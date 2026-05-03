# Week 4: Multi-Language Code Generation & LLM Integration

## Overview

Week 4 focuses on **leveraging LLMs for cross-language code generation and execution**, building a system that can convert algorithms between Python, C++, Rust, and Go. This week combines LLM API integration, compiler management, performance benchmarking, and interactive web interfaces using Gradio.

### Key Themes
- 🤖 **LLM-Driven Code Generation**: Using APIs from Groq, OpenRouter, and Gemini
- 🔄 **Multi-Language Transpilation**: Converting algorithms between Python, C++, Rust, and Go
- ⚡ **Performance Benchmarking**: Comparing execution times across languages
- 🛠️ **Cross-Platform Compilation**: Handling Windows, macOS, and Linux compilation
- 🎨 **Interactive Web UI**: Building Gradio-based interfaces for code generation and execution
- 💾 **System Inspection**: Collecting system information for optimization

---

## Directory Structure

```
week4/
├── day4.ipynb                      # Day 4: Intro to LLM-based code generation
├── day5.ipynb                      # Day 5: Advanced multi-language conversion
├── python_to_go_generator.ipynb    # Specialized: Python → Go conversion
├── main.cpp                        # Example C++ benchmark program
├── main.rs                         # Example Rust benchmark program
├── system_info.py                  # System diagnostics & compiler detection
├── styles.py                       # Gradio UI styling (CSS themes)
└── src/
    ├── __init__.py                 # Package initialization
    ├── llm_client.py               # LLM API factory & unified interface
    ├── compiler.py                 # Cross-platform compilation helpers
    ├── code_utils.py               # Code cleaning & execution utilities
    └── ...
```

---

## Core Components

### 1. **LLM Client Factory** (`src/llm_client.py`)

Provides a unified interface for multiple LLM providers through OpenAI-compatible APIs:

| Provider | Base URL | Use Case |
|----------|----------|----------|
| **Groq** | `https://api.groq.com/openai/v1` | Fast inference, cost-effective |
| **OpenRouter** | `https://openrouter.ai/api/v1` | Access to multiple models via single endpoint |
| **Gemini** | `https://generativelanguage.googleapis.com/v1beta/openai/` | Google's latest models |

**Key Functions:**
- `build_clients()` - Initializes all available providers from environment variables
- `call_llm()` - Unified API call with automatic markdown fence stripping
- `check_required_keys()` - Validates API key availability

**Environment Variables Required:**
```
GROQ_API_KEY              # Groq API key
OPENROUTER_API_KEY        # OpenRouter API key
GOOGLE_API_KEY            # Google Gemini API key
```

---

### 2. **Compiler Management** (`src/compiler.py`)

Handles cross-platform compilation and execution for C++, Rust, and Go:

#### **C++ Compilation** (`get_cpp_commands()`)
- **Compilers Supported**: clang++, g++
- **Windows**: Generates `.exe` with optimization flags
- **Unix/Linux/macOS**: Uses C++17 with LTO optimization
- **Auto-detection**: Searches PATH for available compilers

**Installation Guide:**
- **Windows (LLVM/Clang)**: `winget install LLVM.LLVM`
- **Windows (MSYS2/GCC)**: `winget install MSYS2.MSYS2`

#### **Rust Compilation** (`get_rust_commands()`)
- Uses `rustc` with release optimization
- Cross-platform support with appropriate executable extensions

#### **Go Compilation** (Supported in advanced notebooks)
- Uses `go build` for native compilation
- Environment variable configuration for cross-compilation

**Error Handling:**
- Returns human-readable error messages
- Detects missing compilers and provides installation instructions
- Captures both stdout and stderr from compilation

---

### 3. **Code Utilities** (`src/code_utils.py`)

Provides code processing and execution helpers:

**Core Functions:**
- `strip_fences(code)` - Removes markdown code blocks that LLMs sometimes emit
  - Handles: ` ```cpp `, ` ```rust `, ` ```go `, ` ```python `, ` ``` `
  
- `write_output(code, filename)` - Safely writes generated code to disk
  - Auto-strips fences before writing
  - Default filename: `main.cpp`

- `run_python(code)` - Executes Python code in isolation
  - Captures stdout and stderr
  - Uses fresh globals dict (no state sharing)
  - Returns error messages if code fails

---

### 4. **System Diagnostics** (`system_info.py`)

Comprehensive system information collection:

**Captures:**
- OS details (Windows/Linux/macOS, version, kernel)
- CPU/Architecture information
- Available compilers and toolchains
- Node.js and Python environments
- Docker availability
- GPU information (if available)

**Use Cases:**
- Optimization recommendations based on hardware
- Compiler availability checks
- Performance benchmarking context
- Environment-specific code generation

---

### 5. **UI Styling** (`styles.py`)

Gradio CSS theme for professional code generation interface:

**Color Scheme:**
- Python: `#209dd7` (Blue)
- C++: `#ecad0a` (Gold)
- Accent: `#753991` (Purple)
- Background: `#161a22` (Dark)
- Text: `#e9eef5` (Light)

**Features:**
- Full-width layout
- Card-based design for code blocks
- Language-specific output coloring
- Hover effects on buttons
- Custom gradient backgrounds for output panels

---

## Benchmark Programs

### **C++ Example** (`main.cpp`)
Implements a mathematical computation benchmark using series approximation:
```cpp
// Calculates: ∑(1/(4i-1) - 1/(4i+1)) * 4
// 200M iterations with timing
double calculate(int iterations, double param1, double param2)
```
- Demonstrates: Computation-heavy workload, high-precision arithmetic
- Typical use: Performance comparison baseline

### **Rust Example** (`main.rs`)
Implements Kadane's algorithm (maximum subarray problem) with LCG random generation:
```rust
fn max_subarray_sum(n: usize, seed: u32, min_val: i32, max_val: i32) -> i64
```
- Demonstrates: Algorithm efficiency, functional programming patterns
- Typical use: Algorithm comparison, memory safety validation

---

## Notebooks Overview

### **day4.ipynb** - LLM-Based Code Generation Fundamentals
**Topics Covered:**
- Setting up LLM clients (Groq, OpenRouter, Gemini)
- Writing effective prompts for code generation
- Compiling generated C++ code
- Capturing and displaying execution results
- Error handling and validation

**Learning Outcomes:**
- Understanding LLM APIs and rate limits
- Prompt engineering for code generation
- Cross-platform compilation basics
- Performance benchmarking

---

### **day5.ipynb** - Advanced Multi-Language Conversion
**Topics Covered:**
- Python → C++ conversion workflows
- Python → Rust conversion workflows
- Performance comparison across languages
- Optimization techniques per language
- Gradio interface for interactive code conversion

**Learning Outcomes:**
- Multi-language algorithm understanding
- Performance optimization strategies
- LLM chain-of-thought reasoning
- Building interactive ML-powered tools

---

### **python_to_go_generator.ipynb** - Specialized Python to Go Conversion
**Topics Covered:**
- Go syntax and idioms
- Goroutines and channels
- Error handling patterns (Go vs Python)
- Building performant CLI tools
- Type system translation

**Learning Outcomes:**
- Go concurrency patterns
- Cross-language idiom mapping
- Syscall and system-level programming
- Deploying compiled Go binaries

---

## Setup Instructions

### **Prerequisites**
```bash
# Python 3.10+
python --version

# Install dependencies
pip install -r ../requirements.txt
# Includes: openai, python-dotenv, gradio, etc.
```

### **Compiler Setup**

#### **Linux/macOS**
```bash
# macOS (using Homebrew)
brew install llvm gcc rust

# Ubuntu/Debian
sudo apt-get install build-essential clang rustc golang-go

# Fedora
sudo dnf install gcc clang rust go
```

#### **Windows**
```powershell
# Option 1: LLVM/Clang
winget install LLVM.LLVM

# Option 2: MSYS2 with GCC
winget install MSYS2.MSYS2
# Then in MSYS2 shell:
pacman -S mingw-w64-ucrt-x86_64-gcc

# Install Rust
winget install Rustlang.Rust

# Install Go
winget install GoLang.Go
```

### **API Key Configuration**
Create a `.env` file in the week4 directory:
```
GROQ_API_KEY=your_groq_key_here
OPENROUTER_API_KEY=your_openrouter_key_here
GOOGLE_API_KEY=your_gemini_key_here
```

### **Running Jupyter Notebooks**
```bash
cd week4
jupyter notebook day4.ipynb
# or
jupyter lab day5.ipynb
```

---

## Practical Workflows

### **Workflow 1: Generate & Benchmark C++ Code**
1. Open `day4.ipynb`
2. Select Groq model and write algorithm prompt
3. LLM generates C++ code
4. Code compiled with optimization flags
5. Results displayed with execution time
6. Compare with Python baseline

### **Workflow 2: Cross-Language Algorithm Conversion**
1. Open `day5.ipynb`
2. Provide Python function implementation
3. Request conversion to C++, Rust, or Go
4. LLM generates idiomatic code per language
5. Compile and run all versions
6. Benchmark performance differences
7. Analyze trade-offs (speed vs code complexity)

### **Workflow 3: Python to Go CLI Tools**
1. Open `python_to_go_generator.ipynb`
2. Describe desired CLI tool in natural language
3. LLM generates Python prototype
4. LLM converts to Go with concurrency
5. Test Go binary with various inputs
6. Package as standalone executable

---

## Key Concepts

### **1. Prompt Engineering for Code Generation**
- Use clear algorithm descriptions
- Provide example inputs/outputs
- Specify language idioms and constraints
- Request performance optimizations
- Include error handling specifications

### **2. Cross-Platform Compilation**
- Detect available compilers at runtime
- Use platform-specific optimization flags
- Handle executable extensions (`.exe` vs binary)
- Manage include paths and linking

### **3. Performance Profiling**
- Use `std::chrono` (C++) for high-precision timing
- Compare wall-clock time across languages
- Account for JIT compilation overhead
- Measure memory usage when relevant

### **4. LLM Chain-of-Thought**
- Request explanation before code
- Break complex problems into steps
- Validate generated code against test cases
- Use multiple models for verification

---

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| "No C++ compiler found" | Missing compiler | Install clang++ or g++ (see setup) |
| API key errors | Missing `.env` file | Create `.env` with valid API keys |
| Markdown fence errors | LLM adds code fences | `strip_fences()` auto-handles this |
| Executable not found | Wrong path after compile | Use `get_cpp_commands()` for platform-specific paths |
| Rate limit errors | Too many API calls | Use `time.sleep()` between calls |
| Rustc not found | Rust not installed | Run `rustup` or use package manager |

---

## Performance Optimization Tips

### **C++ Optimizations**
- Use `-Ofast` or `-O3` compiler flags
- Enable `-march=native` for CPU-specific optimizations
- Use `-flto=thin` for link-time optimization
- Define `-DNDEBUG` to disable assertions

### **Rust Optimizations**
- Compile with `--release` flag
- Use `#[inline]` for small functions
- Leverage compiler's auto-vectorization
- Profile with `perf` or `flamegraph`

### **Python Optimizations**
- Use NumPy for numerical code
- Consider PyPy for CPU-bound tasks
- Use list comprehensions over loops
- Benchmark with `timeit` module

---

## Learning Resources

### **Official Documentation**
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Groq API Docs](https://console.groq.com/docs)
- [Rust Book](https://doc.rust-lang.org/book/)
- [Go Tour](https://go.dev/tour/welcome/1)
- [Gradio Docs](https://gradio.app/)

### **Algorithm References**
- Bailey–Borwein–Plouffe formula (π approximation)
- Kadane's algorithm (max subarray)
- Linear congruential generators (PRNG)

---

## Next Steps & Extensions

1. **Add PyPy support** for accelerated Python execution
2. **Implement code caching** to avoid duplicate compilations
3. **Create performance dashboard** with visualization
4. **Add version control** for generated code
5. **Build collaborative features** for team code generation
6. **Support additional languages** (C#, Java, TypeScript)
7. **Implement unit test generation** from specifications
8. **Add static analysis** (linting, type checking) to pipeline

---

## Contributing

When adding new features:
- Update this README with new components
- Add docstrings to all functions
- Include type hints (Python 3.9+ syntax)
- Test on Windows, Linux, and macOS
- Validate with multiple LLM providers
- Document new API keys or environment variables

---

## Week 4 Checklist

- [ ] Install all required compilers (C++, Rust, Go)
- [ ] Set up API keys for LLM providers
- [ ] Run `day4.ipynb` and generate first C++ program
- [ ] Successfully compile and execute generated code
- [ ] Complete `day5.ipynb` multi-language conversion
- [ ] Benchmark performance across languages
- [ ] Explore `python_to_go_generator.ipynb`
- [ ] Experiment with different prompts and models
- [ ] Build custom Gradio interface for code generation

---

**Last Updated**: 2025  
**Status**: Active (Jupyter notebooks and utilities fully functional)
