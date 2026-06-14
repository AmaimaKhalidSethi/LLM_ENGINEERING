# Week 6 — "The Price is Right" Capstone Project

## Overview

This week focuses on building price-prediction models from product descriptions. We progress through five days, stepping from data curation and preprocessing all the way to fine-tuning frontier LLMs. The capstone uses Amazon product data (title, category, description, weight, and price) and explores baselines, traditional ML, neural networks, and finally GPT fine-tuning.

---

## Week Progression: Day 1 → Day 5

### **Day 1: Data Curation** — [day1.ipynb](day1.ipynb)

**Goal:** Explore and curate the raw Amazon Reviews 2023 dataset.

**What We Did:**
- Loaded the McAuley-Lab Amazon-Reviews-2023 dataset (raw_meta_Appliances category)
- Investigated dataset structure and investigated individual data points
- Identified data quality issues: missing values, price formatting inconsistencies, outliers
- Found maximum price items and understood price distribution
- Prepared a smaller, cleaned subset for downstream tasks

**Key Learnings:**
- Data curation is the foundation; garbage in = garbage out
- Real datasets are messy — prices come in various formats (floats, strings, missing)
- Need to filter and validate before any ML model can work

**Outputs:** Raw data exploration, identification of data quality issues

---

### **Day 2: Data Pre-processing** — [day2.ipynb](day2.ipynb)

**Goal:** Rewrite raw product data into a standardized format using LLMs.

**What We Did:**
- Loaded curated items from Hugging Face Hub in both "lite" (20K) and "full" (800K) modes
- Used LiteLLM (OpenAI, Groq, Ollama compatibility layer) to invoke LLM summarization
- Implemented batch processing (`Batch` and `batch_local.py`) for large-scale preprocessing
- Each item was transformed from raw scraped data into a clean, structured `Item` object with:
  - **title**, **category**, **price** (raw)
  - **summary** (LLM-generated clean description)
  - **prompt** (formatted for downstream models)
- Pushed cleaned datasets back to Hugging Face Hub (`items_lite`, `items_full`)

**Key Techniques:**
- Batch APIs for cost-effective LLM preprocessing at scale
- Data standardization pipeline (raw → structured objects)
- Hub integration for dataset versioning and sharing

**Outputs:** Cleaned, standardized datasets published to HF Hub

---

### **Day 3: Evaluation, Baselines, Traditional ML** — [day3.ipynb](day3.ipynb)

**Goal:** Build an evaluation framework and test simple baseline models.

**What We Did:**
- **Created the Evaluation Framework:** `pricer/evaluator.py` with:
  - `Tester` class for running price predictors on test sets
  - Plotly scatter plots: predicted vs. actual price (y vs. ŷ)
  - Error trend charts with 95% confidence intervals
  - Metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), R² score
- **Tested Baseline Models:**
  1. **Random Pricer:** Random prices 1–1000 → baseline of ~$200+ average error
  2. **Constant Pricer:** Always predict training average → ~$100+ average error
  3. **Feature-Based Linear Regression:** Weight, text_length, weight_unknown features → improved over constant
  4. **Scikit-learn CountVectorizer + RandomForest:** Text features from product summaries
- **Evaluation Metrics Explained:**
  - **MSE:** Penalizes large errors quadratically (lower is better)
  - **R² Score:** Proportion of variance explained (closer to 1.0 is better)

**Key Learnings:**
- Always establish baselines before complex models
- Visualization (scatter plots) reveals overfitting, underfitting, systematic bias
- Simple feature engineering (weight, text length) beats pure randomness

**Outputs:** Evaluation harness, baseline performance benchmarks

---

### **Day 4: Neural Networks & LLMs** — [day4.ipynb](day4.ipynb)

**Goal:** Move beyond traditional ML to deep learning and LLM-based pricing.

**What We Did:**
1. **Human Pricer Baseline:**
   - Exported test products to `human_in.csv`
   - Collected manual human price estimates → `human_out.csv`
   - Human pricer as a calibration baseline

2. **PyTorch Neural Networks:**
   - Built 8-layer feed-forward neural network with ReLU activations
   - Used HashingVectorizer (binary bag-of-words, 5000 features)
   - Training pipeline: DataLoader, Adam optimizer, L1 loss, learning rate scheduling
   - Demonstrated how neural networks learn non-linear relationships

3. **LLM-Based Pricing (Zero-Shot):**
   - Prompted GPT models to estimate prices from product descriptions
   - Compared LLM predictions with neural network and traditional ML
   - Observed that pre-trained LLMs have surprising price-estimation ability without fine-tuning

**Architectures:**
- Neural net: 5000 → 128 → 64 (×6) → 1
- Batch processing to avoid memory overflow on large datasets

**Outputs:** Trained neural net, LLM zero-shot predictions, comparative metrics

---

### **Day 5: Fine-Tuning a Frontier Model** — [day5.ipynb](day5.ipynb)

**Goal:** Fine-tune GPT-4 Nano to specialize in price prediction.

**What We Did:**
1. **Prepared Fine-Tuning Dataset:**
   - Selected 100 training examples + 50 validation examples from the main dataset
   - Converted to JSONL format (OpenAI's fine-tuning format):
     ```json
     {
       "messages": [
         {"role": "user", "content": "Estimate the price of this product. Respond with the price, no explanation\n\n{summary}"},
         {"role": "assistant", "content": "$XX.XX"}
       ]
     }
     ```
   - Uploaded training and validation files to OpenAI via their API

2. **Fine-Tune Job Submission:**
   - Used `openai.fine_tuning.jobs.create()` to submit fine-tune job
   - Model: `gpt-4o-mini-2024-07-18` (cost ~$3.42 for 100 examples)
   - Monitored job status, retrieved model ID when complete

3. **Evaluation:**
   - Loaded fine-tuned model and ran inference on test set
   - Compared fine-tuned model performance vs. zero-shot GPT
   - Fine-tuned model specialized to price-prediction task

**Cost & Performance:**
- Fine-tuning cost: ~$3.42 (100 training examples)
- Time: A few minutes for the job to run
- Improvement: Fine-tuned model focused on numeric output; reduced verbosity

**Outputs:** Fine-tuned GPT model, performance metrics, JSONL training data in `jsonl/` folder

---

## Project Structure & Key Files

```
week6/
├── day1.ipynb                      # Data curation from Amazon Reviews
├── day2.ipynb                      # LLM-based data preprocessing
├── day3.ipynb                      # Evaluation framework & baselines
├── day4.ipynb                      # Neural networks & LLMs
├── day5.ipynb                      # Fine-tuning GPT-4 Nano
│
├── redemption_train.ipynb          # Optional: Deep neural net training (4+ hours)
├── redemption_run.ipynb            # Optional: Load pretrained DNN & evaluate
├── results.ipynb                   # Summary visualizations
│
├── pricer/                         # Core package
│   ├── items.py                    # Item dataclass, HF Hub I/O
│   ├── evaluator.py                # Evaluation harness, Plotly charts
│   ├── deep_neural_network.py      # PyTorch ResNet-style DNN (optional)
│   ├── batch.py, batch_local.py    # Batch preprocessing with LLMs
│   ├── preprocessor.py             # Data cleaning utilities
│   ├── parser.py                   # Parsing raw product data
│   ├── loaders.py                  # Dataset loading helpers
│   └── test_batch_smoke.py         # Unit tests
│
├── jsonl/                          # Fine-tuning datasets
│   ├── 0_1000.jsonl                # Sample dataset
│   ├── fine_tune_train.jsonl       # Training data for fine-tune job
│   └── fine_tune_validation.jsonl  # Validation data
│
├── full/, full/batches/, full/output/
│                                   # Large batch processing outputs
│
├── human_in.csv, human_out.csv     # Test products & human price estimates
│
└── README.md                       # This file
```

---

## Performance Summary

**Model Rankings (Approximate MAE):**
1. **Fine-Tuned GPT-4 Nano:** ~$50–70 MAE ⭐ (after 100-example fine-tune)
2. **Zero-Shot LLM (GPT-4o):** ~$80–120 MAE (no training needed)
3. **PyTorch Neural Net:** ~$60–100 MAE (depends on architecture & hyperparams)
4. **Random Forest + Text Features:** ~$120–150 MAE
5. **Constant Pricer:** ~$100+ MAE
6. **Random Pricer:** ~$200+ MAE

*Note: Exact numbers depend on test set, model variant, and hyperparameters. See `results.ipynb` for full breakdown.*

---

## Setup & Requirements

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

Includes: `huggingface_hub`, `openai`, `litellm`, `torch`, `scikit-learn`, `plotly`, `datasets`, `tqdm`, `pydantic`.

### 2. Environment Variables
Create a `.env` file (or set in your shell):
```
HF_TOKEN=hf_xxxxx...        # Hugging Face API token
OPENAI_API_KEY=sk-xxxxx...  # OpenAI API key
```

### 3. Data Mode
Both lite and full modes available:
- **Lite:** 20K items, fast & cheap (~$1 to preprocess)
- **Full:** 800K items, comprehensive (~$30 to preprocess)

Toggle in notebooks:
```python
LITE_MODE = True   # or False for full dataset
```

---

## Quick Start Commands

### Run Day-by-Day Notebooks
```powershell
# Day 1: Data exploration (no cost)
jupyter notebook week6/day1.ipynb

# Day 2: Preprocessing (small cost ~$1 for lite, $30 for full)
jupyter notebook week6/day2.ipynb

# Day 3: Evaluation & baselines (no cost)
jupyter notebook week6/day3.ipynb

# Day 4: NN & LLMs (optional cost ~$2–5 for zero-shot LLM calls)
jupyter notebook week6/day4.ipynb

# Day 5: Fine-tuning (cost ~$0.50–3 depending on examples)
jupyter notebook week6/day5.ipynb
```

### Run Optional Deep NN Training (Long-Running)
```powershell
# Training takes 4–6 hours on M1 Mac; longer on CPU
jupyter notebook week6/redemption_train.ipynb

# Then evaluate with pretrained weights
jupyter notebook week6/redemption_run.ipynb
```

### Run Unit Tests
```powershell
pytest week6/pricer/test_batch_smoke.py -q
```

### Generate Results Summary
```powershell
jupyter notebook week6/results.ipynb
```

---

## Key Concepts Covered

| Concept | Day(s) | File(s) |
|---------|--------|---------|
| Data Curation | 1 | `day1.ipynb` |
| Batch Processing (LLM-based) | 2 | `day2.ipynb`, `pricer/batch*.py` |
| Evaluation Framework (MAE, MSE, R²) | 3 | `pricer/evaluator.py` |
| Baseline Models | 3 | `day3.ipynb` |
| Neural Networks (PyTorch) | 4 | `day4.ipynb`, `pricer/deep_neural_network.py` |
| Zero-Shot LLM Prompting | 4 | `day4.ipynb` |
| Fine-Tuning OpenAI Models | 5 | `day5.ipynb` |
| Plotly Visualization | 3–5 | `pricer/evaluator.py` |

---

## Common Issues & Troubleshooting

**Q: Datasets not loading from HF Hub?**  
A: Check that `HF_TOKEN` is set correctly. Run `huggingface-cli login` if needed.

**Q: `trust_remote_code` deprecation error in Day 1?**  
A: Update datasets: `pip install --upgrade datasets==3.6.0` and restart kernel.

**Q: Out of memory during training?**  
A: Use `LITE_MODE = True` or reduce batch size in training loops.

**Q: Fine-tuning job stuck or failed?**  
A: Check OpenAI quota and billing. View job details with:
```python
from openai import OpenAI
client = OpenAI()
client.fine_tuning.jobs.list()
```

**Q: Plotly charts not displaying?**  
A: Ensure you're running in a Jupyter environment. Plotly is interactive HTML-based.

---

## Extending This Project

### Ideas for Week 6+ Work
1. **Hyperparameter Tuning:** Experiment with different neural net architectures, learning rates, batch sizes.
2. **Cross-Validation:** Use k-fold CV to get more robust performance estimates.
3. **Ensemble Models:** Combine fine-tuned LLM + neural net + tree-based models.
4. **Category-Specific Models:** Fine-tune separate models for Electronics, Furniture, etc.
5. **A/B Testing:** Deploy multiple models and compare live predictions.
6. **Explainability:** Use SHAP or LIME to understand which features drive predictions.

### Community Solutions
Check [community-contributions/](community-contributions/) for 100+ student submissions with alternate approaches:
- Different architectures (ResNets, transformers)
- Alternative datasets and preprocessing
- Frontier model experiments (Gemini, Claude)
- Advanced fine-tuning strategies

---

## References & Resources

- **OpenAI Fine-Tuning Docs:** https://platform.openai.com/docs/guides/fine-tuning
- **Hugging Face Datasets:** https://huggingface.co/docs/datasets
- **PyTorch Tutorial:** https://pytorch.org/tutorials
- **Scikit-Learn ML:** https://scikit-learn.org
- **Plotly Charts:** https://plotly.com/python

---

## Summary: What We Built

Over 5 days, we built a **price-prediction system** that:
1. **Curated** messy real-world product data
2. **Preprocessed** it with LLMs into a clean, standardized format
3. **Evaluated** performance with rigorous metrics and visualizations
4. **Experimented** with baselines, ML, and deep learning
5. **Fine-tuned** a frontier LLM to specialize in price estimation

**Best Model:** Fine-tuned GPT-4 Nano (~$50–70 MAE)  
**Key Insight:** LLMs are surprisingly good at price estimation without fine-tuning, and fine-tuning makes them even better.

---

**Last Updated:** Week 6 (LLM Engineering Bootcamp)  
**For Questions:** Refer to each day's notebook for detailed explanations and code comments.
