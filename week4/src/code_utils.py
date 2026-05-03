"""
code_utils.py
=============
Shared utilities for:
  - Stripping markdown code fences from LLM output.
  - Writing generated code to disk.
  - Executing Python code strings in-process and capturing stdout.

Used by: day4.ipynb, day5.ipynb, python_to_go_generator.ipynb
"""

import io
import re
import sys


# ─────────────────────────────────────────────────────────────────────────────
# Fence stripping
# ─────────────────────────────────────────────────────────────────────────────

def strip_fences(code: str) -> str:
    """
    Remove markdown code fences that LLMs sometimes emit despite instructions.

    Handles:
        ```cpp ... ```
        ```rust ... ```
        ```go ... ```
        ```python ... ```
        ``` ... ```
    """
    code = code.strip()
    # Remove a leading fence line (```<lang> or just ```)
    code = re.sub(r"^```[a-zA-Z+\-]*\r?\n?", "", code)
    # Remove a trailing fence
    code = re.sub(r"\n?```\s*$", "", code)
    return code.strip()


# ─────────────────────────────────────────────────────────────────────────────
# File I/O
# ─────────────────────────────────────────────────────────────────────────────

def write_output(code: str, filename: str = "main.cpp") -> None:
    """
    Write *code* to *filename*, stripping stray markdown fences first.

    Args:
        code:     Raw LLM output (may contain fences).
        filename: Destination path (default ``main.cpp``).
    """
    clean = strip_fences(code)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(clean)


# ─────────────────────────────────────────────────────────────────────────────
# In-process Python execution
# ─────────────────────────────────────────────────────────────────────────────

def run_python(code: str) -> str:
    """
    Execute *code* as a Python string, capturing and returning its stdout.

    Returns an ``"Error: ..."`` string if the code raises an exception.

    Note: Uses ``exec()`` in a fresh globals dict — does **not** share state
    with the notebook kernel.
    """
    globals_dict: dict = {"__builtins__": __builtins__}
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        exec(code, globals_dict)  # noqa: S102
        output = buffer.getvalue()
    except Exception as exc:  # noqa: BLE001
        output = f"Error: {exc}"
    finally:
        sys.stdout = old_stdout
    return output