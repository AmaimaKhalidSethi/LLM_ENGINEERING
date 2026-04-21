# Week 3: Cloud Compute & The HuggingFace Ecosystem

## Overview
Week 3 transitions from using pre-built APIs to leveraging **cloud GPU compute** and working directly with **open-source models** through HuggingFace. Students gain hands-on experience running transformer models on powerful hardware (Google Colab T4 GPUs) and learn the high-level APIs that make deploying models accessible. This week emphasizes building production-ready applications with state-of-the-art open-source models.

## Key Learning Outcomes
- Set up and use Google Colab for free GPU computing
- Connect to HuggingFace Hub and authenticate securely
- Use HuggingFace Pipelines for inference tasks
- Understand transformer model architecture at a practical level
- Optimize model inference for speed and memory
- Deploy models on cloud GPUs

---

## Day-by-Day Breakdown

### **Day 1: Google Colab & GPU Fundamentals**
**File:** `day1.ipynb`

**Content Summary:**
This notebook introduces **Google Colab**, a free cloud Jupyter environment with GPU access. Rather than running models locally (which requires expensive hardware), students learn to leverage Google's infrastructure for model experimentation.

**Key Concepts:**

**What is Google Colab?**
- Browser-based Jupyter notebook running on Google's servers
- **Free tier**: Access to T4 GPUs (compute power equivalent to $500+ GPUs)
- Automatic package management (pip installs)
- Shareable links for collaboration
- Runtime resets if idle (prevent GPU hogging)

**Colab Survival Guide:**
1. **Connect to GPU**: Top-right dropdown → "Connect to hosted runtime" → Select T4
2. **Verify GPU**: Run `!nvidia-smi` to confirm T4 available
3. **Monitor Resources**: View resources menu to watch memory usage
4. **Handle Disconnects**: Runtime can reset; always run installs from top

**Key Logic & Implementations:**

**GPU Detection:**
```python
!pip install transformers==4.56.2 diffusers==0.32.2

!nvidia-smi  # Verify Tesla T4 GPU
```

**HuggingFace Authentication:**
- Create free account at `https://huggingface.co`
- Generate "Write" access token with full permissions
- Store securely in Colab Secrets (not in code)
- Use `userdata.get('HF_TOKEN')` to retrieve safely

**Primary Learning Outcomes:**
- Cloud GPU infrastructure for ML work
- Secure credential management in cloud environments
- Handling session resets and runtime management
- Leveraging free tier GPU compute

**Technologies Used:** Google Colab, nvidia-smi, HuggingFace authentication

---

### **Day 2: HuggingFace Pipelines & Transformers**
**File:** `day2.ipynb`

**Content Summary:**
HuggingFace Transformers library provides **high-level APIs** (Pipelines) that abstract away complexity. Rather than manually loading models, tokenizing, and managing tensors, pipelines let students write simple code like:

```python
classifier = pipeline("text-classification")
result = classifier("I love this!")  # Returns: [{'label': 'POSITIVE', 'score': 0.99}]
```

**What is a Pipeline?**
A Pipeline is an abstraction that wraps:
1. **Tokenizer**: Text → Token IDs
2. **Model**: Token IDs → Predictions
3. **Post-processor**: Raw outputs → Human-readable results

All bundled into a single function call.

**Key Logic & Implementations:**

**Common Pipeline Tasks:**
```python
# Text Classification
sentiment = pipeline("sentiment-analysis")
sentiment("This is great!")  # → POSITIVE

# Named Entity Recognition (NER)
ner = pipeline("ner")
ner("John Smith works at OpenAI")  # → ['PERSON', 'ORG']

# Question Answering
qa = pipeline("question-answering")
qa(question="Where do I work?", context="I work at OpenAI")

# Text Generation
generator = pipeline("text-generation")
generator("Once upon a time")  # → Continues story

# Zero-shot Classification
classifier = pipeline("zero-shot-classification")
classifier("I love pizza", candidate_labels=["Food", "Sports", "Technology"])
```

**Model Selection:**
- HuggingFace Hub hosts 100,000+ models
- Default models are auto-downloaded and cached
- Students can swap models with one line: `pipeline("task", model="specific-model-id")`

**Pro Tips for Colab:**
1. **Ignore warnings**: Many warnings are safe in cloud notebooks
2. **Runtime errors**: If you get CUDA errors, it's often a Colab reset — just restart the kernel
3. **Disk space**: Models are cached in `/root/.cache/huggingface/`
4. **Memory monitoring**: Use "View Resources" during long-running tasks

**Primary Learning Outcomes:**
- High-level API hides complexity without sacrificing power
- Task-driven model selection
- Efficient inference on GPUs
- Understanding when to use pipelines vs. custom implementations

**Technologies Used:** HuggingFace Transformers, Pipelines, Colab GPUs

---

## Advanced Topics (Implicit in Notebooks)

### **Model Architecture Understanding**
While Week 3 focuses on *using* models via Pipelines, the notebooks build intuition about:
- **Attention mechanisms**: How transformers focus on relevant tokens
- **Token embeddings**: Text representation as vectors
- **Model layers**: Stacking transformers for deeper reasoning
- **Fine-tuning**: Adapting pre-trained models to custom tasks

### **Inference Optimization**
Beyond basic usage, advanced patterns include:
- **Batch processing**: Inferring on multiple samples simultaneously
- **Quantization**: Reducing model precision (float32 → int8) for speed
- **Pruning**: Removing less important parameters
- **Caching**: Reusing KV cache for faster generation

---

## Key Concepts Introduced This Week

| Concept | Definition | Week 3 Context |
|---------|-----------|-------------------|
| **GPU** | Graphics Processing Unit; 100x faster for matrix operations | Free T4 in Colab runs transformers 10-50x faster than CPU |
| **HuggingFace Hub** | Central repository of 100k+ models and datasets | Download and use models with one line |
| **Pipeline** | High-level API wrapping tokenizer + model + post-processor | `pipeline("task-name")` handles all complexity |
| **Transformers** | Deep learning architecture excelling at NLP | Backbone of GPT, BERT, all modern LLMs |
| **Tokenizer** | Converts text → model-readable tokens | Automatic within pipelines |
| **Model Context Window** | Max tokens a model can process at once | GPT-4 supports 128K tokens, Mistral 8K |
| **Inference** | Running a trained model on new data | vs. "training" which updates model weights |
| **Batch Inference** | Processing multiple samples simultaneously | More efficient than one-by-one |

---

## Architecture: Cloud ML Pipeline

```
Week 3 Cloud Architecture:
┌────────────────────────────────────────┐
│   Google Colab (Browser)               │
│  - Write Python code                   │
│  - Access GPU automatically            │
└────────────────┬───────────────────────┘
                 │
        ┌────────▼────────┐
        │   HuggingFace   │
        │   Secrets Store │ (Secure API tokens)
        └────────┬────────┘
                 │
        ┌────────▼──────────────┐
        │ HuggingFace Hub       │
        │ (Model Repository)    │
        │ - Mistral, Llama, etc │
        └────────┬──────────────┘
                 │
        ┌────────▼──────────────┐
        │  Colab T4 GPU         │
        │ - Load model weights  │
        │ - Run inference       │
        │ - Cache activations   │
        └───────────────────────┘
```

---

## HuggingFace Pipelines Reference

### **Natural Language Understanding (NLU)**
```python
# Sentiment Analysis
pipeline("sentiment-analysis")

# Text Classification (custom labels)
pipeline("zero-shot-classification")

# Named Entity Recognition
pipeline("ner")

# Question Answering
pipeline("question-answering")

# Text Summarization
pipeline("summarization")
```

### **Natural Language Generation (NLG)**
```python
# Text Generation
pipeline("text-generation", model="mistral")

# Machine Translation
pipeline("translation_en_to_fr")

# Text-to-Speech
pipeline("text-to-speech")
```

### **Multimodal**
```python
# Image Classification
pipeline("image-classification")

# Visual Question Answering
pipeline("visual-question-answering")

# Image-to-Text
pipeline("image-to-text")
```

---

## Best Practices for Colab

### **1. GPU Management**
```python
import torch
print(f"GPU available: {torch.cuda.is_available()}")
print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

### **2. Secure Credentials**
```python
from google.colab import userdata
hf_token = userdata.get('HF_TOKEN')  # Stored safely, not in code

from huggingface_hub import login
login(token=hf_token)
```

### **3. Model Caching**
```python
# Models auto-cache after first download
# Check cache location
from transformers import AutoModel
model = AutoModel.from_pretrained("mistral-7b")  # Downloads once, cached
```

### **4. Efficient Inference**
```python
# Batch processing
inputs = ["Text 1", "Text 2", "Text 3"]
results = classifier(inputs)  # More efficient than one-by-one

# Model device placement
model = model.to("cuda")  # Ensure on GPU
```

---

## Common Colab Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| CUDA out of memory | Model too large for GPU | Use smaller model variant; clear cache |
| Model not found | Wrong model ID on HF Hub | Check exact name on huggingface.co |
| Connection reset | Idle timeout | Keep code running; can't leave notebook dormant >30min |
| Import errors | Missing packages | Run pip install cells at notebook top |
| Slow inference | CPU fallback | Verify GPU with `!nvidia-smi`; check `device` parameter |

---

## Week 3 Use Cases

### **1. Document Classification**
```python
classifier = pipeline("zero-shot-classification")
doc = "New quantum computing breakthrough..."
labels = ["Tech", "Sports", "Politics"]
classifier(doc, labels)
```

### **2. Q&A from Text**
```python
qa = pipeline("question-answering")
context = "The Great Wall of China is 13,000 miles long"
qa(question="How long is the Great Wall?", context=context)
```

### **3. Text Summarization**
```python
summarizer = pipeline("summarization")
article = "Long article text..."
summarizer(article, max_length=100)
```

### **4. Named Entity Recognition**
```python
ner = pipeline("ner")
text = "Apple CEO Tim Cook announced..."
ner(text)  # → [{'entity': 'ORG', 'word': 'Apple'}, ...]
```

---

## Performance Considerations

### **Inference Speed**
- **T4 GPU**: ~100-500 inferences/sec (depending on model)
- **CPU**: ~5-20 inferences/sec
- **GPU advantage**: 10-100x faster

### **Memory Usage**
- **Mistral 7B**: ~15 GB VRAM
- **Llama 13B**: ~26 GB VRAM
- **Colab T4**: 16 GB VRAM (fits smaller models easily)

### **Cost**
- **Colab Free**: $0/month (best for learning)
- **Colab Pro**: $10/month (longer runtimes, better GPU)
- **Local GPU**: $300-3000 (one-time hardware cost)

---

## Integration with Previous Weeks

### **Week 1 → Week 3**
- Week 1: Used API-based LLMs (OpenAI, Groq)
- Week 3: Direct model access (can fine-tune, customize)
- **Advantage**: Full control, no API costs, privacy

### **Week 2 → Week 3**
- Week 2: Built interfaces for API-based models
- Week 3: Same interfaces work with local HuggingFace models
- **Code reuse**: Can swap out provider without changing UI

---

## Graduation Path

After Week 3, students are equipped to:
1. **Build production ML systems** on cloud GPUs
2. **Fine-tune models** on custom data
3. **Deploy models** for real-world applications
4. **Contribute to HuggingFace Hub** with custom models
5. **Scale inference** with frameworks like vLLM, Ray

---

## Additional Resources

- **HuggingFace Model Hub**: https://huggingface.co/models
- **Transformers Documentation**: https://huggingface.co/docs/transformers
- **Colab Help**: https://colab.research.google.com
- **GPU Compute Guide**: https://colab.research.google.com/#scrollTo=3-6UJaKF0tKw

---

## Next Steps

Post Week 3:
- **Fine-tuning**: `transformers.Trainer` for custom tasks
- **Deployment**: FastAPI + Docker for production
- **Optimization**: Quantization and pruning for efficiency
- **Advanced Architectures**: Vision transformers, multimodal models
