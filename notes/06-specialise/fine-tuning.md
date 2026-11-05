# Fine-tuning

*Choose a Specialisation › LLMs & Generative AI* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#fine-tuning)

> **In one sentence:** Fine-tuning continues training a pretrained model on your examples so it learns your task or style.

## Key ideas
- Try prompting and RAG first; fine-tune when you need a consistent style, format or a smaller, cheaper model.
- Quality beats quantity: a few hundred clean examples can be enough.
- LoRA/QLoRA train small adapter weights, so it fits on a single GPU.
- Hold out test examples and compare against the base model.

## Example
```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
name = "distilbert-base-uncased"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name, num_labels=2)
ds = load_dataset("imdb").map(lambda b: tok(b["text"], truncation=True), batched=True)
Trainer(model=model, args=TrainingArguments("out", num_train_epochs=1),
        train_dataset=ds["train"].shuffle(seed=0).select(range(2000)),
        eval_dataset=ds["test"].select(range(500)), tokenizer=tok).train()
```

## Common mistakes
- Fine-tuning to add facts (use RAG for knowledge).
- No evaluation set, so you can't tell if it improved.

## Learn more
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) · Free · Course

## Practice project
Fine-tune a small model to write replies in Roman Urdu.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
