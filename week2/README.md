# Week 2: Multi-Model Integration & Interactive Applications

## Overview
Week 2 focuses on **scaling beyond a single LLM provider** and building **interactive user interfaces**. Students learn to connect to multiple frontier models simultaneously (OpenAI, Groq, Gemini, DeepSeek, etc.), compare their capabilities, and wrap everything in user-friendly web applications using Gradio. The week emphasizes practical decision-making: knowing which model to use for which task.

## Key Learning Outcomes
- Connect to multiple frontier LLM providers via unified APIs
- Understand training-time vs. inference-time scaling strategies
- Build interactive web interfaces with Gradio
- Create stateful chatbot applications with multi-turn memory
- Evaluate and compare model performance across different providers

---

## Day-by-Day Breakdown

### **Day 1: Multi-Provider Model Integration**
**File:** `day1.ipynb`

**Content Summary:**
This notebook demonstrates connecting to multiple cutting-edge LLM providers through a single unified interface. Instead of being locked into one provider, students learn to flexibly switch between models based on availability, cost, or performance needs.

**Supported Providers:**
- **OpenAI**: `gpt-4`, `gpt-4-turbo` (official OpenAI cloud)
- **Groq**: `llama-3.3-70b-versatile` (fast open-source alternative, free tier)
- **Google Gemini**: `gemini-3.1-flash-lite-preview` (Google's vision/multimodal models)
- **DeepSeek**: Chinese frontier model with strong reasoning
- **Grok**: X.AI's latest model
- **OpenRouter**: Aggregator service supporting 100+ models
- **Ollama**: Local models (free, private)

**Key Logic & Implementations:**
```python
# Unified API setup pattern
openai = OpenAI()  # Uses OPENAI_API_KEY
groq = OpenAI(api_key=groq_key, base_url=groq_url)  # Different endpoint
gemini = OpenAI(api_key=google_key, base_url=gemini_url)  # OpenAI-compatible
```

**Primary Learning Outcomes:**
- All major providers expose OpenAI-compatible interfaces
- Environment variable management for multiple API keys
- Fallback strategies when primary provider is unavailable
- Cost comparison between providers (OpenAI expensive, Groq free, Ollama local)

**Featured Task:** "Tell a joke" request demonstrating identical message format across all providers

**Technologies Used:** OpenAI SDK, dotenv, multiple API endpoints

---

### **Day 2: Introduction to Gradio**
**File:** `day2.ipynb`

**Content Summary:**
Gradio is a Python framework for rapidly building web-based interfaces for ML models. Rather than manually building HTML/CSS/JavaScript, Gradio handles the UI automatically. This notebook introduces the basics of wrapping LLM endpoints in interactive applications.

**Key Logic & Implementations:**

**Provider Setup:**
- Configures Groq and Gemini APIs
- Builds helper functions to interact with each:
```python
def message_groq(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    response = groq.chat.completions.create(...)
    return response.choices[0].message.content
```

**Gradio Interface:**
- Input elements (text boxes, sliders, dropdowns)
- Output elements (text, images, markdown)
- Function binding: Each input triggers a backend function

**Primary Learning Outcomes:**
- Rapid prototyping of AI applications without web development skills
- Clean separation between backend (LLM) and frontend (UI)
- Easy deployment of interactive demos
- Real-time interface updates from model responses

**Technologies Used:** Gradio, OpenAI SDK, Groq, Gemini

---

### **Day 3: Conversational AI & Chatbots**
**File:** `day3.ipynb`

**Content Summary:**
This notebook extends Gradio to create a **full-featured chatbot** with persistent conversation memory. Unlike Day 2's stateless examples, Day 3 builds applications where the AI remembers previous exchanges.

**Key Logic & Implementations:**

**Message Management:**
- Maintain `messages` list across interface interactions
- Append new user messages
- Store and display assistant responses
- System prompt defines chatbot personality

**Stateful Gradio Application:**
```python
def chat_interface(user_input, chat_history):
    # chat_history persists across calls
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_input})
    
    response = llm.chat.completions.create(...)
    
    chat_history.append({"role": "assistant", "content": response})
    return chat_history  # Update UI with full conversation
```

**Multi-Model Chatbot:**
- Users can switch between providers (Groq, Gemini, etc.)
- Same conversation history applies across models
- Compare how different models respond to identical prompts

**Primary Learning Outcomes:**
- Stateful applications where context persists
- Handling multi-turn conversations in UI
- Responsive chat interfaces
- Model switching mid-conversation

**Technologies Used:** Gradio, OpenAI SDK, Message history patterns

---

### **Day 4.1: Advanced Model Integration**
**File:** `day4.1.ipynb`

**Content Summary:**
This notebook explores more sophisticated patterns for multi-model interactions:
- Chaining multiple LLMs in sequence (output of one feeds input of next)
- Parallel queries to multiple models for comparison
- Caching responses to reduce API costs
- Fine-tuning and adaptation strategies

**Key Concepts:**
- **Training-time vs. Inference-time Scaling**:
  - Larger models perform better with minimal reasoning ("System 1" thinking)
  - Smaller models need more reasoning steps ("System 2" thinking)
  - Can dial up inference compute to fix small model weaknesses
- **Competitive Model Testing**: Benchmarks to compare models on reasoning tasks

**Primary Learning Outcomes:**
- Trade-offs between model size and reasoning budget
- How to structure queries for optimal model performance
- Model selection strategies based on task complexity

**Technologies Used:** Multiple LLM APIs, response parsing, comparison metrics

---

### **Day 4.2: Advanced Chaining & Optimization**
**File:** `day4.2.ipynb`

**Content Summary:**
Continuation of Day 4.1 with deeper dives into:
- **Chain-of-Thought** prompting (asking models to show reasoning)
- **Few-Shot Learning** (providing examples in prompts)
- **Retrieval Augmented Generation** (RAG) patterns
- **Response Optimization** techniques

**Primary Learning Outcomes:**
- Structured prompting for consistent output
- Context injection via examples
- Performance optimization strategies
- Monitoring and debugging multi-model systems

---

### **Day 5.1 & Day 5.2: Capstone Projects**
**Files:** `day5.1.ipynb`, `day5.2.ipynb`

**Content Summary:**
Extended application building combining all Week 2 skills:
- Building production-ready chatbot systems
- Deploying multi-model interfaces
- Adding persistence (conversation logging)
- Monitoring API costs and performance

---

### **Extra Resources**
**File:** `extra.ipynb`

Additional materials, advanced patterns, and reference implementations for deeper exploration.

---

## Key Concepts Introduced This Week

| Concept | Definition | Week 2 Application |
|---------|-----------|-------------------|
| **Model Enumeration** | Listing available models from each provider | Supporting user choice: "Use Groq" vs "Use Gemini" |
| **Provider Abstraction** | Single code works across multiple LLM APIs | `openai` library supports 10+ provider endpoints |
| **Fallback Logic** | Using backup provider if primary fails | Primary: OpenAI → Fallback: Groq (free) |
| **Chatbot State** | Maintaining conversation history in UI | `chat_history` list persists across Gradio interactions |
| **Inference Scaling** | Adjusting reasoning steps without changing model | "n_reasoning_steps" parameter to boost accuracy |
| **UI Binding** | Connecting Python functions to web elements | Gradio `Interface` or `ChatInterface` decorators |
| **Real-time Streaming** | Displaying LLM output as it generates | Gradio's built-in streaming support for better UX |

---

## Architecture: Multi-Model Chatbot System

```
Week 2 Final Architecture:
┌─────────────────────────────────────────┐
│        Gradio Web Interface              │
│  (Text input, chat history display)      │
└────────────┬──────────────────────────────┘
             │
┌────────────▼──────────────────────────────┐
│    Chatbot Logic Layer                    │
│  (Message management, state handling)     │
└────────────┬──────────────────────────────┘
             │
    ┌────────┴─────────┬──────────────┬─────────┐
    │                  │              │         │
 ┌──▼──┐          ┌───▼───┐      ┌──▼──┐  ┌──▼──┐
 │Groq │          │Gemini │      │ GPT │  │Local│
 │(API)│          │(API)  │      │(API)│  │Ollam│
 └──────┘          └───────┘      └─────┘  └─────┘

All connected via OpenAI-compatible endpoints
```

---

## Advanced Patterns Covered

### **1. Model Switching**
```python
selected_provider = gr.Radio(choices=["Groq", "Gemini", "GPT"])
# Chat function selects appropriate LLM based on user choice
```

### **2. Conversation Persistence**
```python
def chat(user_message, chat_history):
    chat_history.append({"role": "user", "content": user_message})
    response = llm.chat.completions.create(messages=chat_history)
    chat_history.append({"role": "assistant", "content": response})
    return chat_history
```

### **3. Cost Optimization**
- Groq is free for many models
- OpenAI charges per token
- Local Ollama has zero API cost
- Strategy: Default to Groq, fall back to alternatives

---

## Practical Decision Matrix

| Task | Recommended Model | Reasoning |
|------|------------------|-----------|
| Quick responses | Groq (free) | Fast inference, cost-effective |
| High quality reasoning | GPT-4 | Strongest reasoning capabilities |
| Multimodal (vision) | Gemini | Built-in vision support |
| Privacy critical | Ollama (local) | Data never leaves your machine |
| Brainstorming | Any | Less critical, minimal cost |
| Production chatbot | Groq + OpenAI fallback | Balance cost and reliability |

---

## Files & Storage

- **`hamlet.txt`**: Text file for testing RAG/document analysis
- **`prices.db`, `prices1.db`**: Sample databases for querying patterns
- **`.gradio/`**: Gradio configuration and cache
- **`workspace.db`**: Session data storage (optional)

---

## Common Implementations

### Pattern 1: Unified Chat Function
```python
def send_message(user_input, model_choice):
    if model_choice == "Groq":
        llm = groq_client
    elif model_choice == "Gemini":
        llm = gemini_client
    else:
        llm = openai_client
    
    response = llm.chat.completions.create(messages=[...])
    return response.choices[0].message.content
```

### Pattern 2: Gradio Chat Interface
```python
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Message")
    submit = gr.Button("Send")
    
    msg.submit(chat_function, [msg, chatbot], [msg, chatbot])
    submit.click(chat_function, [msg, chatbot], [msg, chatbot])

demo.launch()
```

---

## Next Steps

Week 3 escalates to:
- **Cloud GPU compute** (Google Colab T4 GPUs)
- **HuggingFace ecosystem** (transformers, pipelines, model hub)
- **Fine-tuning and custom models**
- **Advanced inference optimization** (quantization, pruning)
