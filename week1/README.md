# Week 1: Foundations of LLM Integration

## Overview
Week 1 establishes the foundational skills for working with Large Language Models (LLMs). The focus is on learning how to interact with different LLM providers through APIs, understanding fundamental concepts like tokenization, and building practical applications that combine web scraping with AI summarization.

## Key Learning Outcomes
- Compare and integrate multiple LLM providers (cloud-based and local)
- Understand LLM tokenization and token counting
- Build conversational AI applications with message history
- Extract and process web content using scraping and LLMs
- Implement streaming responses for real-time AI interactions

---

## Day-by-Day Breakdown

### **Day 1: Comparing LLM Providers - Gemini vs Ollama**
**File:** `day_1.ipynb`

**Content Summary:**
This notebook introduces two contrasting LLM approaches:
- **Google Gemini**: Cloud-based API requiring authentication
- **Ollama**: Local LLM runtime for free, private inference

**Key Logic & Implementations:**
- Setting up OpenAI-compatible clients for different providers
- Configuring API endpoints (`base_url`, `api_key`)
- Testing both providers with identical API calls
- Comparing the trade-offs between cloud and local solutions

**Primary Learning Outcomes:**
- Understanding provider abstraction through OpenAI SDK compatibility
- Evaluating cost (API fees) vs. privacy (local execution) trade-offs
- Recognizing that different LLM providers expose the same interface

**Technologies Used:** OpenAI SDK, Python `dotenv` for secret management

---

### **Day 2: Ollama Setup & Web Content Extraction**
**File:** `day2.ipynb`

**Content Summary:**
This notebook demonstrates practical LLM applications by combining web scraping with AI analysis. Students learn to:
- Set up Ollama locally and verify the OpenAI-compatible endpoint
- Build a `Website` class to scrape and parse web content
- Use LLMs to analyze and summarize extracted text

**Key Logic & Implementations:**
- **Web Scraping**: Using `BeautifulSoup` to parse HTML and extract clean text
  - Removes boilerplate (scripts, styles, images)
  - Extracts title and body content
- **LLM Integration**: System prompts guide the model to analyze website content
- **System Prompts**: Instructing the LLM on behavior (e.g., "You are an assistant that analyzes website contents")

**Primary Learning Outcomes:**
- Building reusable utility classes for web interaction
- Crafting effective system prompts for targeted AI behavior
- Understanding the role of system vs. user messages in conversations

**Technologies Used:** BeautifulSoup, Requests, Ollama, OpenAI SDK

---

### **Day 4: Tokenization & Conversation Memory**
**File:** `day4.ipynb`

**Content Summary:**
This notebook covers two critical concepts:
1. **Tokenization**: Understanding how LLMs break down text into tokens
2. **Conversation Memory**: Managing message history to simulate context awareness

**Key Logic & Implementations:**

**Tokenization Section:**
- Using `tiktoken` to encode and decode text
- Inspecting individual token IDs and their text representations
- Understanding token boundaries and chunking patterns
- Token ID 65 = 'A' (ASCII mapping for context)

**Conversation Memory Section:**
- Maintaining a persistent `messages` list across turns
- Adding user and assistant messages to simulate "memory"
- Understanding the "illusion of memory" — the model doesn't truly remember, it just sees all prior messages in context

**Message Structure:**
```python
messages = [
    {"role": "system", "content": "Instructions for the AI"},
    {"role": "user", "content": "First user message"},
    {"role": "assistant", "content": "AI response (from history)"},
    {"role": "user", "content": "Next user message"}
]
```

**Primary Learning Outcomes:**
- Tokenization limits prompt size and API costs
- Message history enables multi-turn conversations
- Context window limitations require awareness of total token count

**Technologies Used:** `tiktoken`, OpenAI SDK, Ollama

---

### **Day 5: Automated Web Brochure Generation**
**File:** `day5.ipynb`

**Content Summary:**
This is a capstone project combining all Week 1 concepts into an end-to-end application:
- Extract website links programmatically
- Use AI to intelligently filter relevant pages
- Aggregate content from multiple pages
- Generate a professional company brochure via LLM

**Key Logic & Implementations:**

**Step 1: Link Extraction**
- `fetch_website_links()` scrapes all hyperlinks from a website

**Step 2: Intelligent Link Filtering**
- System prompt instructs the LLM to identify relevant pages (About, Careers, Pricing)
- JSON structured output: `response_format={"type": "json_object"}`
- Excludes noise (Privacy, Terms of Service, email links)

**Step 3: Content Aggregation**
- Fetches full text content from each relevant link
- Organizes content by link type (markdown structure)

**Step 4: Brochure Generation**
- LLM analyzes aggregated content with a system prompt
- Generates markdown-formatted brochure
- **Streaming**: Real-time display of response as it's generated

**Primary Learning Outcomes:**
- End-to-end automation combining multiple AI techniques
- Structured output generation (JSON) for reliable parsing
- Streaming responses for better user experience
- Practical prompt engineering with examples and constraints

**Technologies Used:** Groq API, OpenAI SDK, Custom scraper module, JSON parsing, Streaming

---

### **Practice Notebook**
**File:** `practice.ipynb`

**Content Summary:**
Hands-on exercises reinforcing Week 1 concepts:
- Setting up connections to various LLM providers
- Building custom classes for API interactions
- Practicing prompt engineering
- Implementing message history patterns

---

## Key Concepts Introduced This Week

| Concept | Definition | Example Use Case |
|---------|-----------|-------------------|
| **API Key Management** | Securely handling credentials via environment variables | `.env` file with `GROQ_API_KEY`, `GOOGLE_API_KEY` |
| **OpenAI Compatibility** | Standard interface for multiple LLM providers | Same code works with Ollama, Gemini, Groq |
| **System Prompts** | Instructions that define AI behavior and expertise | "You are a helpful assistant that analyzes websites..." |
| **Tokenization** | Breaking text into model-readable units (tokens) | "Hello world" → tokens [9906, 1917] |
| **Message History** | Maintaining conversation context | Passing all prior messages in `messages` list |
| **Structured Output** | Constraining LLM responses to JSON format | `response_format={"type": "json_object"}` |
| **Web Scraping** | Extracting content from HTML | BeautifulSoup to remove noise and extract text |
| **Streaming** | Real-time output as the model generates | Displaying responses character-by-character |

---

## Project Architecture

```
Week 1 Projects:
├── Provider Comparison (Day 1)
│   └── Compare Gemini vs Ollama costs/benefits
├── Web Content Extraction (Day 2)
│   └── Website class → scrape → summarize
├── Tokenization & Memory (Day 4)
│   └── Understand token limits & conversation context
└── Automated Brochure Generator (Day 5)
    ├── Extract links
    ├── Filter with AI
    ├── Aggregate content
    └── Generate brochure
```

---

## Prerequisites & Setup

- Python 3.8+
- API Keys (in `.env`):
  - `GROQ_API_KEY` - For Groq LLM access
  - `GOOGLE_API_KEY` - For Google Gemini (optional)
- Ollama installed and running (`ollama run llama3.2`)
- Python packages from `requirements.txt`:
  - `openai` - OpenAI SDK
  - `python-dotenv` - Environment variables
  - `beautifulsoup4` - Web scraping
  - `requests` - HTTP requests
  - `tiktoken` - Tokenization

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Ollama connection refused | Ensure `ollama run llama3.2` is running in terminal |
| API key errors | Check `.env` file exists and has correct format |
| Token limit exceeded | Reduce message history or use smaller prompts |
| Web scraping blocked | Use User-Agent header in requests (included in notebooks) |

---

## Next Steps
Week 1 establishes core competencies. Week 2 builds on these by:
- Connecting to **multiple frontier models** simultaneously
- Building **interactive UIs** with Gradio
- Creating **conversational chatbots** with stateful memory
