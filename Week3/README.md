# Week 3: Cloud Compute & The HuggingFace Ecosystem

## Overview
Week 3 transitions from API-based models to direct model access and cloud GPU computing. Students learn to use Google Colab for free GPU access, authenticate with HuggingFace, understand tokenization, work with transformer models, and build real-world applications like audio transcription and meeting minutes generation.

## Key Learning Outcomes
- Set up Google Colab and connect to T4/A100 GPUs
- Authenticate securely with HuggingFace Hub
- Understand tokenization and token prediction
- Load and run transformer models with quantization
- Work with multiple model architectures (Llama, Phi, Gemma, Qwen, DeepSeek)
- Process audio and generate structured outputs
- Optimize inference for memory and speed

---

## Day-by-Day Breakdown

### **Day 1: Google Colab & Generative Models**
**File:** `day1.ipynb`

**Topics:**
- Google Colab setup and runtime management
- Connecting to free T4 GPUs and paid A100 GPUs
- HuggingFace authentication with secure tokens
- Image generation with Stable Diffusion (SDXL, Turbo, Refiner)
- Text-to-speech synthesis
- FLUX.1 model demonstration
- Cost estimation for cloud GPU usage

**Key Concepts:**
- Free T4 tier limitations and reset behavior
- HuggingFace token management (Write permissions required)
- Model pipeline usage with diffusers library
- Paid tier benefits and pricing ($9.99 = 100 compute units)
- Kernel management (restart vs. disconnect + delete)

**Technologies:** Google Colab, NVIDIA GPUs, HuggingFace, Diffusers, Stable Diffusion, FLUX.1

---

### **Day 2: HuggingFace Pipelines & Transformers**
**File:** `day2.ipynb`

**Topics:**
- HuggingFace Pipelines abstraction layer
- Common inference tasks (sentiment analysis, NER, QA, text generation, translation, summarization)
- Pipeline architecture (tokenizer → model → post-processor)
- Model selection strategies
- Streaming responses and optimization

**Key Concepts:**
- Pipelines simplify model usage to single function calls
- Understanding pipeline flow: text → tokens → embeddings → predictions → results
- Selecting appropriate models for specific tasks
- Managing inference on limited hardware

**Technologies:** HuggingFace Transformers, Pipelines, PyTorch

---

### **Day 3: Tokenizers & Token Prediction**
**File:** `day3.ipynb` and `day5_visualizetokens.ipynb`

**Topics:**
- Understanding tokenization process
- Character, word, and token counting
- Chat templates and instruct model formats
- Comparing tokenizers across different models
- Token ID conversion
- Model-specific prompt formatting

**Key Concepts:**
- Tokenizers break text into sub-word tokens
- Different models use different tokenization schemes
- Chat templates standardize message formatting for instruction-tuned models
- Message structure conversion: Python dicts → formatted text → tokens → token IDs
- Token efficiency varies by model architecture

**Models Analyzed:**
- Meta-Llama-3.1 (8B and 1B variants)
- Microsoft Phi-4
- DeepSeek-V3.1
- Qwen2.5-Coder-7B

**Technologies:** AutoTokenizer, HuggingFace Transformers

---

### **Day 4: Models & Transformer Architecture**
**File:** `Day4.ipynb`

**Topics:**
- Loading models with BitsAndBytes quantization
- Understanding Transformer neural network architecture
- Model inference with streaming output
- Memory optimization and garbage collection
- Comparing multiple models side-by-side
- Quantization configuration (4-bit, bfloat16)

**Key Concepts:**
- Quantization reduces memory footprint while maintaining performance
- Transformer architecture: embedding layers → decoder blocks → attention → MLPs → output
- Model streaming enables token-by-token output display
- Memory management critical for resource-constrained environments
- Generation parameters (max_tokens, temperature, top_p)

**Models Tested:**
- Meta-Llama-3.1-8B-Instruct
- Microsoft Phi-4-mini-instruct
- Google Gemma-3-270m-it
- Qwen3-4B-Instruct
- DeepSeek-R1-Distill-Qwen-1.5B

**Technologies:** AutoModelForCausalLM, BitsAndBytes, TextStreamer, PyTorch quantization

---

### **Day 5: Audio Processing & Real-World Applications**
**File:** `day5.ipynb`

**Topics:**
- Audio transcription (Whisper vs. OpenAI API)
- LLM-based text analysis and structuring
- Meeting minutes generation with action items
- Google Drive integration
- End-to-end workflow: audio → transcription → analysis → structured output

**Key Concepts:**
- Speech-to-text models (Whisper-medium) can run locally on GPUs
- OpenAI transcription API for comparison
- Streaming model output for real-time response display
- System prompts for structured output generation
- Long-context processing with large token limits

**Project Workflow:**
1. Load audio file from Google Drive
2. Transcribe using Whisper or OpenAI
3. Analyze transcript with Llama 3.2
4. Generate meeting minutes with attendees, discussion points, and action items
5. Display formatted markdown output

**Technologies:** Speech2Text Whisper, OpenAI API, Llama, Google Drive integration

---

## Tech Stack Summary

**Cloud Infrastructure:**
- Google Colab (CPU, T4 GPU, A100 GPU)
- Google Drive storage integration

**Model Libraries:**
- HuggingFace Transformers (loading and inference)
- Diffusers (image generation)
- BitsAndBytes (quantization)

**Models Covered:**
- **Text Generation**: Llama 3.1/3.2, Phi-4, DeepSeek, Qwen
- **Image Generation**: Stable Diffusion XL, FLUX.1
- **Speech**: Whisper (transcription), SpeechT5 (synthesis)
- **Vision**: Through pipelines for multi-modal tasks

**Key Features:**
- 4-bit quantization for memory efficiency
- Streaming outputs for interactive responses
- Chat templates for instruction-tuned models
- GPU memory optimization with garbage collection

---

## Project Outputs

- **Generative Models**: Images created with SDXL and FLUX.1
- **Speech Synthesis**: AI-generated voices using SpeechT5
- **Meeting Minutes**: Structured documents with action items from audio transcriptions
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
