# Exploratory data analysis

*Data Skills* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#eda)

> **In one sentence:** Exploratory data analysis means looking before you model: find patterns, problems and surprises.

## Key ideas
- Start with shape, types, missing values and target balance.
- Plot every important column's distribution, then the target against each feature.
- Look for leakage: a feature that is suspiciously perfect usually contains the answer.
- Write findings as sentences; each should change what you do next.

## Example
```python
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
df = sns.load_dataset("tips")
print(df.describe(include="all").T)
sns.boxplot(data=df, x="day", y="tip"); plt.title("Tips are highest on Sundays"); plt.show()
```

## Common mistakes
- Skipping EDA and going straight to models.
- Making 50 charts and no conclusions.

## Learn more
- [Kaggle Learn: Data Visualization](https://www.kaggle.com/learn/data-visualization) · Free · Course

## Practice project
Write a one-page EDA report with five findings and one chart each.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
