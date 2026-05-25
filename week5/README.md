# Week 5: Building a RAG-Based Expert Knowledge Worker

## Overview

Week 5 focused on implementing **Retrieval-Augmented Generation (RAG)**, a powerful technique for building accurate, cost-effective question-answering systems powered by LLMs. The project built an expert knowledge worker assistant for **Insurellm**, a fictional insurance tech company, helping employees quickly find accurate answers about company products, employees, and contracts.

## Learning Objectives

By the end of Week 5, you learned:
- How to structure and organize knowledge bases for LLM applications
- Document chunking strategies for optimal retrieval
- Vector embeddings and semantic search using Chroma
- Building production-quality RAG pipelines with LangChain
- Evaluating RAG systems comprehensively (retrieval and answer quality)
- Advanced RAG techniques for maximum accuracy and efficiency
- Building user interfaces with Gradio

## Daily Breakdown

### Day 1: Introduction to RAG and Knowledge Base Management

**Concepts Covered:**
- RAG fundamentals: Why RAG improves accuracy and reduces costs
- Knowledge base structure and organization
- Simple keyword-based retrieval

**Practical Implementation:**
- Loaded employee and product data from markdown files
- Built a simple keyword-matching function to retrieve relevant context
- Created a basic chatbot using Gradio and OpenRouter's Llama model
- Demonstrated how simple keyword matching can work as a baseline RAG approach

**Key Files:**
- `day1.ipynb` - Basic RAG implementation with keyword matching

---

### Day 2: Document Chunking and Vector Embeddings

**Concepts Covered:**
- Token counting and document statistics using tiktoken
- Document chunking strategies with `RecursiveCharacterTextSplitter`
- Vector embeddings using HuggingFace's `all-MiniLM-L6-v2` model
- Storing and persisting vectors in Chroma database
- Visualizing high-dimensional vectors with t-SNE

**Practical Implementation:**
- Analyzed the entire knowledge base (character and token count)
- Loaded all markdown files using LangChain's DirectoryLoader
- Split documents into 1000-character chunks with 200-character overlap
- Created embeddings for all chunks using HuggingFace's lightweight model
- Persisted vector database to disk for reuse
- Generated 2D visualization of vector space for exploration

**Key Metrics:**
- Knowledge base size analysis
- Chunk statistics and overlap
- Vector database size and organization

**Key Files:**
- `day2.ipynb` - Chunking, embeddings, and vector database creation
- `vector_db/` - Persistent Chroma database with embeddings

---

### Day 3: LangChain RAG Pipeline

**Concepts Covered:**
- LangChain abstractions for RAG (Retriever, LLM, Messages)
- System prompts and context formatting
- Chat interface with history support
- Temperature parameter and model configuration

**Practical Implementation:**
- Connected to pre-built Chroma vector store
- Created a retriever object for semantic search
- Integrated with OpenRouter's Llama 3.3 70B model
- Built complete pipeline: query → retrieve → augment → generate
- Developed Gradio UI with chat interface and context display
- Implemented history tracking for multi-turn conversations

**Architecture:**
```
User Question
    ↓
Retrieve Similar Documents (Chroma)
    ↓
Format Context into System Prompt
    ↓
LLM Response with Augmented Context
    ↓
Display with Source Attribution
```

**Key Files:**
- `day3.ipynb` - Complete LangChain RAG pipeline
- `implementation/answer.py` - Core answer generation logic
- `app.py` - Gradio application for the RAG system

---

### Day 4: Evaluation and Quality Metrics

**Concepts Covered:**
- Retrieval evaluation metrics:
  - **Mean Reciprocal Rank (MRR)**: How high is the correct document ranked?
  - **NDCG (Normalized Discounted Cumulative Gain)**: Quality of ranking
  - **Keyword Coverage**: How many search keywords appear in results?
- Answer evaluation using LLM-as-a-judge:
  - **Accuracy**: Factual correctness (1-5 scale)
  - **Completeness**: All information addressed (1-5 scale)
  - **Relevance**: Answer quality and appropriateness (1-5 scale)
- Dashboard with color-coded metrics

**Practical Implementation:**
- Created test dataset with 50+ test questions across multiple categories
- Implemented retrieval evaluation against reference documents
- Built LLM-based answer evaluator using Groq's inference
- Developed Gradio dashboard with metrics visualization
- Color-coded thresholds (green/orange/red) for quick assessment
- Aggregated metrics by category and overall

**Evaluation Framework:**
- Test categories: Employee queries, Product queries, Contract queries, General knowledge
- Retrieval evaluation: Measured ranking quality
- Answer evaluation: LLM-as-a-judge with detailed feedback

**Key Files:**
- `day4.ipynb` - Evaluation framework and metrics
- `evaluation/eval.py` - Evaluation logic
- `evaluation/test.py` - Test data and utilities
- `evaluation/tests.jsonl` - Test question dataset
- `evaluator.py` - Gradio dashboard for evaluation results

---

### Day 5: Advanced RAG Techniques (Going Pro!)

**Concepts Covered:**
- Building without LangChain for maximum flexibility and control
- Intelligent document chunking using LLM
- Document preprocessing and rewriting
- Chunk ranking and reranking for better retrieval
- Multiprocessing for scalable ingest pipelines
- Production-ready code patterns

**Practical Implementation:**

#### Basic Advanced Pipeline:
- Native Chroma API without LangChain wrappers
- Pydantic models for structured chunk representation
- LLM-powered chunk generation with headlines and summaries
- Each chunk includes:
  - **Headline**: Few words most likely in queries
  - **Summary**: 2-3 sentences answering common questions
  - **Original Text**: Unchanged source material

#### Professional Pipeline:
- Multiprocessing for parallel chunk generation (3 workers)
- Retry logic with exponential backoff for API resilience
- Reranking using LLM to order chunks by relevance
- RetrievalK=20 candidates → Reranked to FINAL_K=10
- OpenAI embeddings (text-embedding-3-large) for better quality
- Smaller average chunk size (100 tokens) for precision

**Architecture (Pro Version):**
```
Documents → LLM Preprocessing → Chunks with metadata
    ↓
Stored in Chroma (native API)
    ↓
Query Retrieval (Top-20 candidates)
    ↓
LLM Reranking (Top-10 final)
    ↓
Answer Generation with Best Context
```

**Key Features:**
- Pydantic validation for data integrity
- Path utilities for cross-platform compatibility
- LiteLLM integration for model flexibility
- Tenacity for robust error handling
- Vector database reuse with `get_or_create_collection()`

**Key Files:**
- `day5.ipynb` - Advanced RAG techniques walkthrough
- `pro_implementation/ingest.py` - Professional ingest pipeline
- `pro_implementation/answer.py` - Professional answer pipeline with reranking
- `preprocessed_db/` - Preprocessed vector database

---

## Project Structure

```
week5/
├── README.md                          # This file
├── app.py                             # Main Gradio application
├── evaluator.py                       # Evaluation dashboard
│
├── day1.ipynb                         # RAG introduction
├── day2.ipynb                         # Chunking & embeddings
├── day3.ipynb                         # LangChain pipeline
├── day4.ipynb                         # Evaluation framework
├── day5.ipynb                         # Advanced techniques
│
├── implementation/                    # Basic RAG implementation
│   ├── answer.py                      # Answer generation
│   └── ingest.py                      # Document ingest
│
├── pro_implementation/                # Professional RAG system
│   ├── answer.py                      # Advanced answer logic
│   └── ingest.py                      # Advanced ingest logic
│
├── evaluation/                        # Evaluation framework
│   ├── eval.py                        # Evaluation metrics
│   ├── test.py                        # Test data handling
│   └── tests.jsonl                    # Test questions dataset
│
├── knowledge-base/                    # Company knowledge base
│   ├── company/                       # Company info
│   ├── contracts/                     # Contract documents
│   ├── employees/                     # Employee profiles
│   └── products/                      # Product information
│
├── vector_db/                         # Chroma vector database (basic)
│   └── chroma.sqlite3
│
├── preprocessed_db/                   # Chroma database (advanced)
│   └── chroma.sqlite3
```

---

## Key Technologies

| Technology | Purpose | Week Used |
|---|---|---|
| **LangChain** | RAG orchestration and abstractions | Days 2-4 |
| **Chroma** | Vector database for embeddings storage | Days 2-5 |
| **HuggingFace** | Lightweight embeddings (`all-MiniLM-L6-v2`) | Days 2-4 |
| **OpenAI/Groq/OpenRouter** | LLM inference for generation and evaluation | All days |
| **Gradio** | Web interface for chatbot and dashboard | Days 1, 3-4 |
| **Pydantic** | Data validation and modeling | Days 5 |
| **LiteLLM** | Unified LLM API across providers | Day 5 |
| **Tenacity** | Retry logic with exponential backoff | Day 5 |

---

## Important Concepts

### RAG (Retrieval-Augmented Generation)
RAG combines retrieval (finding relevant documents) with generation (creating answers) to make LLMs more accurate and cost-effective.

**Benefits:**
- ✅ Lower hallucination rates
- ✅ More up-to-date information
- ✅ Cost-effective (reuse cheaper LLMs with better context)
- ✅ Easier to debug and iterate

### Chunking Strategy
Good chunking is critical for RAG success:
- Chunks too small: Lose context
- Chunks too large: Dilute signal in embeddings
- Week 5 used 500-1000 character chunks with overlap
- Advanced approach: LLM-generated summaries improve retrieval

### Vector Embeddings
- Convert text into numerical vectors
- Similar meaning → similar vectors (cosine similarity)
- Enables semantic search beyond keywords
- Trade-off: Speed vs. quality (larger models are slower)

### Evaluation Matters
- Always evaluate both retrieval AND answer quality
- Can't see retrieval issues through answer quality alone
- LLM-as-a-judge is practical for at-scale evaluation
- Color-coded dashboards help identify problem areas

---

## Running the Applications

### Basic RAG Chatbot
```bash
# Run the basic implementation
python app.py
```
Opens Gradio interface with chat and context display.

### Evaluation Dashboard
```bash
# Run the evaluator
python evaluator.py
```
Shows retrieval and answer quality metrics across test questions.

---

## Key Insights

1. **Foundation Matters**: Day 1-2 fundamentals (chunking, embeddings) are critical
2. **Evaluation is Essential**: Metrics reveal what's actually working
3. **Reranking Works**: Re-ranking top-K candidates improves answer quality significantly
4. **Temperature ≠ Creativity**: Use system prompts for creativity, not temperature
5. **Iteration is Key**: Good RAG systems evolve through testing and evaluation

---

## Week 5 Learning Progression

```
Day 1: Basic keyword matching
  ↓ Learn why it fails
Day 2: Add vectors & semantic search
  ↓ Way better but missing framework
Day 3: Build production RAG with LangChain
  ↓ Works well but want more control
Day 4: Evaluate systematically
  ↓ Now we know what's working/failing
Day 5: Go advanced - intelligent chunking & reranking
  ↓ Maximum accuracy and efficiency
```

---

## Next Steps (Week 6+)

- Fine-tuning retrieval with query rewriting
- Multi-hop reasoning for complex questions
- Adding filtering and metadata-based search
- Streaming responses for better UX
- Advanced chain-of-thought prompting
- Cost optimization and caching strategies

---

## Summary

Week 5 transformed you from a RAG novice to understanding production-quality systems. You learned that RAG success depends on three pillars: **good data organization** (chunking), **effective retrieval** (embeddings + databases), and **rigorous evaluation** (metrics that matter). The progression from keyword matching to intelligent preprocessing and reranking shows how each improvement compounds.

The key takeaway: **In RAG, the details matter**. The difference between a 50% accurate and 95% accurate system often comes down to chunking strategy, prompt engineering, and evaluation rigor—not just model selection.
