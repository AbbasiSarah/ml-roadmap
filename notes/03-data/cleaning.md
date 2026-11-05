# Data cleaning

*Data Skills* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#cleaning)

> **In one sentence:** Most ML time is spent cleaning data, and a model is only as good as its data.

## Key ideas
- Check: missing values, duplicates, wrong types, impossible values (age 250), inconsistent labels ("Lhr" vs "Lahore").
- Decide per column: drop, fill (median/most frequent), or flag as a feature ("was missing").
- Remove exact duplicates *before* splitting train/test, or the test set leaks.
- Keep a log of every change, so others can trust your result.

## Example
```python
import pandas as pd
df = pd.read_csv("messy.csv")
df = df.drop_duplicates()
df["city"] = df["city"].str.strip().str.title().replace({"Lhr": "Lahore"})
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df.loc[~df["age"].between(0, 110), "age"] = None
df["age"] = df["age"].fillna(df["age"].median())
```

## Common mistakes
- Filling missing values using statistics from the *whole* dataset, test rows included (leakage).
- Silently dropping rows without counting how many.
- Fixing data by hand in Excel, so nobody can repeat it.

## Learn more
- [Kaggle Learn: Data Cleaning](https://www.kaggle.com/learn/data-cleaning) · Free · Course

## Practice project
Find and fix every problem in a messy dataset, and write down what you changed.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
