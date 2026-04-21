# LLM Engineering: Mastering Generative AI

A comprehensive course covering LLM fundamentals, API integration, multi-model systems, cloud compute, and production deployment.

## 📚 Course Overview

| Week | Focus | Key Skills | Files |
|------|-------|-----------|-------|
| **Week 1** | LLM Fundamentals & APIs | Multi-provider APIs, tokenization, web scraping, prompt engineering | [Details](./week1/README.md) |
| **Week 2** | Multi-Model Systems & UIs | Provider selection, Gradio apps, stateful chatbots | [Details](./week2/README.md) |
| **Week 3** | Cloud Compute & Open-Source | Google Colab, HuggingFace, transformers, audio processing | [Details](./week3/README.md) |

---

## 🚀 Quick Start

Each week contains daily notebooks structured as follows:

- **Day 1-4**: Core concepts and hands-on implementation
- **Day 5**: Capstone project integrating week's topics
- **Extra notebooks**: Advanced topics and alternative approaches

### Prerequisites
- Basic Python knowledge
- API keys for: OpenAI, HuggingFace (free), Google Colab (free)
- No GPU required initially (Weeks 1-2); GPU needed for Week 3

### How to Use
1. Navigate to the week folder
2. Read the README for that week
3. Run notebooks in order (Day 1 → Day 5)
4. Refer to detailed documentation in each week's README

---

## 📖 Week Summaries

### Week 1: LLM Fundamentals & API Integration
Learn to work with multiple LLM providers (OpenAI, Groq, Gemini, Ollama) through unified APIs. Build projects including web scrapers, content summarizers, and automated pipelines.

**Key Topics:** SDK setup, tokenization, prompt engineering, streaming, web scraping

---

### Week 2: Multi-Model Integration & Interactive Applications  
Connect to multiple frontier models and build interactive Gradio web interfaces. Explore stateful chatbots, model selection strategies, and deployment patterns.

**Key Topics:** Gradio UI, multi-provider setups, chatbot memory, model evaluation

---

### Week 3: Cloud Compute & Open-Source Models
Use free Google Colab GPUs to run transformer models directly from HuggingFace. Process audio, generate images, and build real-world applications with quantized models.

**Key Topics:** Google Colab, GPU management, HuggingFace authentication, tokenizers, model inference, audio processing

---

## 🛠️ Technologies Used

**Models & Frameworks:**
- HuggingFace Transformers, Diffusers
- OpenAI, Groq, Gemini, DeepSeek APIs
- Ollama (local models)
- PyTorch, Llama, Phi, DeepSeek models

**Infrastructure:**
- Google Colab (free T4 GPUs)
- Gradio (web UIs)
- BeautifulSoup (web scraping)

**Cloud & Deployment:**
- Google Drive integration
- Model quantization (BitsAndBytes)

---

## 📁 Project Structure

```
LLM_ENGINEERING/
├── week1/          # API fundamentals & automation
├── week2/          # Multi-model & Gradio UIs
├── week3/          # Cloud GPUs & transformers
└── README.md       # This file
```

Each week includes a dedicated README with detailed breakdowns of daily content and learning outcomes.
│ ✓ Web scraping & content processing                     │
│ ✓ Streaming responses                                   │
│ ✓ System prompts & message history                      │
│ └─→ Capstone: Automated Brochure Generator              │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│ WEEK 2: Scale & UI                                      │
├─────────────────────────────────────────────────────────┤
│ ✓ Multi-provider integration                            │
│ ✓ Model enumeration & selection                         │
│ ✓ Gradio web interfaces                                 │
│ ✓ Stateful applications                                 │
│ ✓ Persistent conversation memory                        │
│ ✓ UI/Backend integration                                │
│ ✓ Model switching mid-application                       │
│ └─→ Capstone: Multi-model Chatbot Application           │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│ WEEK 3: GPU & Open-Source                               │
├─────────────────────────────────────────────────────────┤
│ ✓ Google Colab GPU setup                                │
│ ✓ HuggingFace Hub authentication                        │
│ ✓ Transformers library                                  │
│ ✓ Pipeline APIs for common tasks                        │
│ ✓ Model inference optimization                          │
│ ✓ GPU memory management                                 │
│ ✓ Batch processing & caching                            │
│ └─→ Capstone: Custom Model Pipeline Application         │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Command line familiarity
- API keys for: Groq (free), Google (optional), OpenAI (optional)

### Setup Instructions

1. **Clone or download this repository**
```bash
cd LLM_ENGINEERING
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API keys** (Create `.env` file in root)
```
GROQ_API_KEY=your_groq_key_here
GOOGLE_API_KEY=your_google_key_here
OPENAI_API_KEY=your_openai_key_here
```

5. **Start with Week 1**
```bash
jupyter notebook week1/day_1.ipynb
```

6. **For Ollama** (optional, recommended for local inference)
```bash
# Install from https://ollama.ai
ollama pull llama3.2
ollama run llama3.2
```

---

## 📊 Skill Progression

### **By End of Week 1**
- [ ] Connect to multiple LLM providers via unified API
- [ ] Write effective system prompts
- [ ] Tokenize text and count tokens
- [ ] Implement message history for conversations
- [ ] Extract and process web content
- [ ] Generate streaming responses
- [ ] Build end-to-end automation pipelines

### **By End of Week 2**
- [ ] Connect to 6+ different LLM providers
- [ ] Select optimal models for tasks
- [ ] Build Gradio web interfaces
- [ ] Create stateful chatbot applications
- [ ] Switch between models mid-conversation
- [ ] Deploy interactive demos
- [ ] Understand training vs. inference scaling

### **By End of Week 3**
- [ ] Set up and use Google Colab GPUs
- [ ] Authenticate with HuggingFace Hub
- [ ] Use transformers library effectively
- [ ] Deploy HuggingFace pipelines
- [ ] Optimize inference for speed/memory
- [ ] Understand transformer architecture
- [ ] Run models on cloud GPUs

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|---------------|
| **LLM APIs** | OpenAI, Groq, Google Gemini, DeepSeek, Grok, OpenRouter |
| **Local Models** | Ollama, HuggingFace Transformers |
| **Python Libraries** | OpenAI SDK, python-dotenv, BeautifulSoup4, Requests |
| **Web Framework** | Gradio |
| **Cloud Platform** | Google Colab (free GPU) |
| **ML Framework** | PyTorch, HuggingFace Transformers |
| **Utilities** | tiktoken (tokenization), Jupyter |

---

## 💡 Key Concepts

### **Week 1 Foundations**
- **Multi-provider Architecture**: Single codebase works with any OpenAI-compatible API
- **System Prompts**: Define AI behavior and expertise
- **Tokenization**: Understanding model input limits
- **Message History**: Creating multi-turn conversations
- **Streaming**: Real-time response display

### **Week 2 Scaling**
- **Provider Selection**: Cost vs. capability trade-offs
- **Stateful Applications**: Persistent user interactions
- **UI Integration**: Separating backend logic from frontend
- **Inference Scaling**: Model size vs. reasoning time

### **Week 3 Advanced**
- **Cloud Compute**: GPU acceleration for inference
- **Model Architecture**: Transformer fundamentals
- **Pipelines**: High-level APIs abstracting complexity
- **Optimization**: Speed and memory efficiency

---

## 📈 Project Examples

### Week 1: Brochure Generator
**Input**: Company website URL  
**Process**: Scrape → Filter links → Aggregate content → Generate brochure  
**Output**: Professional markdown document

### Week 2: Multi-Model Chatbot
**Input**: User text + Model selection  
**Process**: Route to selected provider → Maintain history → Stream response  
**Output**: Interactive web interface with persistent memory

### Week 3: Document Classifier
**Input**: Document + Label set  
**Process**: Load transformer pipeline → Batch process → Display results  
**Output**: Zero-shot classification on GPU

---

## 📝 Project Structure

```
LLM_ENGINEERING/
├── week1/
│   ├── README.md                 ← Week 1 documentation
│   ├── day_1.ipynb              (Gemini vs Ollama)
│   ├── day2.ipynb               (Web scraping + summarization)
│   ├── day4.ipynb               (Tokenization & memory)
│   ├── day5.ipynb               (Brochure generator)
│   ├── practice.ipynb            (Exercises)
│   ├── scraper.py               (Web scraping utilities)
│   └── output.txt               (Sample outputs)
│
├── week2/
│   ├── README.md                 ← Week 2 documentation
│   ├── day1.ipynb               (Multi-provider setup)
│   ├── day2.ipynb               (Gradio basics)
│   ├── day3.ipynb               (Chatbot with Gradio)
│   ├── day4.1.ipynb             (Advanced integration)
│   ├── day4.2.ipynb             (Chaining & optimization)
│   ├── day5.1.ipynb             (Capstone part 1)
│   ├── day5.2.ipynb             (Capstone part 2)
│   ├── extra.ipynb              (Reference implementations)
│   ├── hamlet.txt               (Test corpus)
│   └── prices.db                (Sample database)
│
├── week3/
│   ├── README.md                 ← Week 3 documentation
│   ├── day1.ipynb               (Colab setup & GPU)
│   └── day2.ipynb               (HuggingFace Pipelines)
│
├── README.md                      ← This file
└── requirements.txt               (Python dependencies)
```

---

## 🔧 Common Tasks

### **Run a Specific Notebook**
```bash
jupyter notebook week1/day_1.ipynb
```

### **Install Additional Packages**
```bash
pip install package-name
```

### **Set API Keys**
Create `.env` in root directory:
```
GROQ_API_KEY=xxx
GOOGLE_API_KEY=xxx
```

### **Use Ollama Locally**
```bash
ollama pull llama3.2
ollama run llama3.2
# Model runs at http://localhost:11434
```

### **Access Colab**
Open notebooks directly in Colab via:
```
https://colab.research.google.com/github/YourUsername/repo/blob/main/week3/day1.ipynb
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| API key not found | Check `.env` file exists and has correct format |
| Ollama connection refused | Run `ollama run llama3.2` in another terminal |
| Token limit exceeded | Reduce message history or use smaller prompts |
| GPU not available in Colab | Ensure runtime is set to "GPU" not "CPU" |
| HuggingFace authentication fails | Verify HF_TOKEN has write permissions |
| Out of memory on GPU | Reduce batch size; use smaller model variant |

---

## 🎓 Learning Outcomes by Week

### **Week 1**: Foundation Builder
- Understand LLM fundamentals and provider landscape
- Build effective prompts and manage conversations
- Create end-to-end automation pipelines
- **You can**: Connect to any LLM API and build working applications

### **Week 2**: System Architect
- Design multi-provider systems with intelligent fallbacks
- Build production-ready web interfaces
- Create stateful conversational applications
- **You can**: Build and deploy interactive AI applications at scale

### **Week 3**: ML Engineer
- Leverage cloud GPU compute for inference
- Understand transformer architecture fundamentals
- Optimize model performance for production
- **You can**: Run and fine-tune state-of-the-art open-source models

---

## 🚀 Next Steps After the Course

1. **Fine-tuning**: Adapt models to your domain using LoRA
2. **Retrieval-Augmented Generation (RAG)**: Add knowledge bases to LLMs
3. **Agents**: Build autonomous AI agents that take actions
4. **Deployment**: Production systems with FastAPI, Docker, Kubernetes
5. **Custom Architectures**: Build your own transformer models

---

## 📚 References & Resources

### **APIs & Services**
- [OpenAI API](https://platform.openai.com)
- [Groq AI](https://groq.com)
- [Google AI Studio](https://makersuite.google.com)
- [HuggingFace Hub](https://huggingface.co)

### **Libraries**
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Gradio Documentation](https://gradio.app)

### **Learning Resources**
- [Attention Is All You Need (Paper)](https://arxiv.org/abs/1706.03762)
- [HuggingFace Course](https://huggingface.co/course)
- [LangChain Documentation](https://python.langchain.com)

---

## 💬 Questions & Support

If you have questions:
1. Check the week-specific README files
2. Review the notebook comments and markdown cells
3. Consult the official documentation links above
4. Run the code and experiment!

---

## 📄 License

This course material is provided as-is for educational purposes.

---

## ✨ Highlights

- **3 weeks** of progressive learning
- **10+ hands-on projects** building real applications
- **6+ LLM providers** covered
- **Free GPU compute** via Google Colab
- **Production-ready patterns** from day one
- **Full code examples** for every concept

---

## 🎯 Final Takeaway

By the end of this course, you'll understand:
- How LLMs work at a practical level
- How to integrate them into applications
- How to scale systems with cloud compute
- How to leverage open-source models
- How to build production AI systems

**Start with [Week 1](./week1/README.md) and build progressively!**

---

**Course Created**: March 2024  
**Last Updated**: April 2026  
**Version**: 1.0
