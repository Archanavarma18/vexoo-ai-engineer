# Vexoo Labs – AI Engineer Assignment

## Overview

This project implements:

* Document ingestion with sliding window
* Knowledge Pyramid (4-layer architecture)
* Query retrieval using similarity scoring
* GSM8K fine-tuning pipeline (LoRA-based)
* Reasoning-aware adapter design (Bonus)

---

## Project Structure

```
.
├── ingestion.py
├── training.py
├── summary.pdf
├── sample_logs.txt
├── bonus_design.txt
└── README.md
```

---

## Part 1: Document Ingestion System

### Features

* Sliding window chunking (overlapping)
* Knowledge Pyramid:

  * Raw Text
  * Summary
  * Category
  * Distilled Keywords
* Query engine with semantic matching

### Run

```bash
python ingestion.py
```

---

## Part 2: GSM8K Training

### Features

* Dataset: GSM8K
* Model: LLaMA 3.2 (LoRA-based fine-tuning)
* Train: 3000 samples
* Test: 1000 samples

### Run

```bash
python training.py
```

---

## Bonus: Reasoning Adapter

Implements a routing-based system:

* Classifies queries (math/legal/general)
* Routes to specialized modules
* Improves reasoning efficiency

---

## Sample Output

See `sample_logs.txt`

---

## Author

Ravali
