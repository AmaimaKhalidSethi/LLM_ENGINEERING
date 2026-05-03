"""
compiler.py
===========
Cross-platform helpers for compiling and running C++, Rust, and Go programs.

All functions return plain strings so they can be displayed directly in
Gradio textboxes or Jupyter cells without extra processing.

Used by: day4.ipynb, day5.ipynb, python_to_go_generator.ipynb
"""

import platform
import shutil
import subprocess
import tempfile
from pathlib import Path

_IS_WINDOWS = platform.system() == "Windows"


# ─────────────────────────────────────────────────────────────────────────────
# C++ helpers
# ─────────────────────────────────────────────────────────────────────────────

def pick_cpp_compiler() -> str:
    """
    Return the first available C++ compiler found on PATH.

    Search order: clang++, g++.

    Raises:
        RuntimeError: if neither compiler is found.
    """
    for candidate in ("clang++", "g++"):
        if shutil.which(candidate):
            return candidate
    raise RuntimeError(
        "No C++ compiler found on PATH.\n"
        "Windows options (pick one):\n"
        "  • LLVM/Clang : winget install LLVM.LLVM\n"
        "  • MSYS2/GCC  : winget install MSYS2.MSYS2  "
        "then inside MSYS2: pacman -S mingw-w64-ucrt-x86_64-gcc\n"
        "After installing, restart your terminal and Jupyter kernel."
    )


def get_cpp_commands(compiler: str | None = None) -> tuple[list[str], list[str]]:
    """
    Return ``(compile_command, run_command)`` for the current platform.

    Args:
        compiler: Override compiler path; auto-detected if ``None``.

    Returns:
        A pair of lists suitable for ``subprocess.run()``.
    """
    if compiler is None:
        compiler = pick_cpp_compiler()

    if _IS_WINDOWS:
        compile_cmd = [compiler, "-O3", "-march=native", "-o", "main.exe", "main.cpp"]
        run_cmd     = ["main.exe"]
    else:
        compile_cmd = [
            compiler, "-std=c++17", "-Ofast", "-march=native",
            "-flto=thin", "-DNDEBUG", "main.cpp", "-o", "main",
        ]
        run_cmd = ["./main"]

    return compile_cmd, run_cmd


def compile_and_run_cpp(
    compile_command: list[str],
    run_command: list[str],
) -> str:
    """
    Compile ``main.cpp`` with *compile_command* and run *run_command*.

    Returns:
        stdout of the compiled program, or a ``"❌ Error: ..."`` string.
    """
    try:
        subprocess.run(compile_command, check=True, text=True, capture_output=True)
        result = subprocess.run(run_command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as exc:
        return f"❌ Compile/run error:\n{exc.stderr}"
    except FileNotFoundError as exc:
        return f"❌ Executable not found: {exc}\nMake sure the compiler is on PATH."


# ─────────────────────────────────────────────────────────────────────────────
# Rust helpers
# ─────────────────────────────────────────────────────────────────────────────

def get_rust_commands(
    rustc_path: str = "rustc",
    source: str = "main.rs",
) -> tuple[list[str], list[str]]:
    """
    Return ``(compile_command, run_command)`` for Rust on the current platform.

    Uses maximum-performance flags:
        -C opt-level=3, target-cpu=native, lto=fat, codegen-units=1,
        panic=abort, strip=symbols.

    Args:
        rustc_path: Full path or name of the ``rustc`` binary.
        source:     Source file to compile (default ``main.rs``).

    Returns:
        A pair of lists suitable for ``subprocess.run()``.
    """
    exe = "main.exe" if _IS_WINDOWS else "main"
    compile_cmd = [
        rustc_path,
        source,
        "-C", "opt-level=3",
        "-C", "target-cpu=native",
        "-C", "codegen-units=1",
        "-C", "lto=fat",
        "-C", "panic=abort",
        "-C", "strip=symbols",
        "-o", exe,
    ]
    run_cmd = [exe] if _IS_WINDOWS else [f"./{exe}"]
    return compile_cmd, run_cmd


def compile_and_run_rust(
    compile_command: list[str],
    run_command: list[str],
) -> str:
    """
    Compile a Rust source file and run the resulting binary.

    Returns:
        stdout of the compiled program, or a ``"❌ Error: ..."`` string.
    """
    try:
        subprocess.run(compile_command, check=True, text=True, capture_output=True)
        result = subprocess.run(run_command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as exc:
        return f"❌ Compile/run error:\n{exc.stderr}"
    except FileNotFoundError as exc:
        return f"❌ Executable not found: {exc}"


# ─────────────────────────────────────────────────────────────────────────────
# Go helpers
# ─────────────────────────────────────────────────────────────────────────────

def run_go_code(go_code: str, timeout: int = 30) -> str:
    """
    Compile and run *go_code* in an isolated temp directory using ``go run``.

    Args:
        go_code:  Complete Go source (``package main`` + ``func main()``).
        timeout:  Seconds before the subprocess is killed (default 30).

    Returns:
        stdout of the Go program, or a ``"❌ / ⚠️ ..."`` error string.
    """
    if not shutil.which("go"):
        return (
            "⚠️  Go compiler not found.\n"
            "Install from https://go.dev/dl/\n"
            "Windows quick install: winget install GoLang.Go\n"
            "Then restart your terminal and Jupyter kernel."
        )

    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "main.go"
        src.write_text(go_code, encoding="utf-8")
        result = subprocess.run(
            ["go", "run", str(src)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if result.returncode != 0:
            return f"❌ Compile/run error:\n{result.stderr}"
        return result.stdout