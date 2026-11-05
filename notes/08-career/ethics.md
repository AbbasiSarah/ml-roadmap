# Responsible AI

*Portfolio & Career* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#ethics)

> **In one sentence:** Responsible AI asks who could be harmed by a model and makes sure results are fair, private and honestly reported.

## Key ideas
- Bias: check performance separately for groups (gender, age, region).
- Privacy: anonymise data and collect only what you need.
- Transparency: explain what the model does and where it fails.
- Honesty: report realistic evaluation, including negative results.

## Example
```python
import pandas as pd
from sklearn.metrics import recall_score
res = pd.DataFrame({"group": groups, "y": y_true, "pred": y_pred})
print(res.groupby("group").apply(lambda g: recall_score(g.y, g.pred)))   # big gaps = investigate
```

## Common mistakes
- Only reporting overall accuracy.
- Using personal data without consent.

## Learn more
- [Kaggle Learn: Intro to AI Ethics](https://www.kaggle.com/learn/intro-to-ai-ethics) · Free · Course

## Practice project
Check one of your models for bias across gender or age groups.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
