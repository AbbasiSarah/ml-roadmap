# Kaggle competitions

*Portfolio & Career* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#kaggle)

> **In one sentence:** Kaggle gives you real datasets, competitions and thousands of public solutions to learn from.

## Key ideas
- Start with "Getting Started" competitions (Titanic, House Prices, Digit Recognizer).
- Read top public notebooks after you try yourself.
- Publish clean notebooks; good ones earn medals and visibility.
- Trust your cross-validation more than the public leaderboard.

## Example
```python
# Typical submission
import pandas as pd
test = pd.read_csv("test.csv")
pd.DataFrame({"Id": test.Id, "SalePrice": model.predict(test[features])}).to_csv("submission.csv", index=False)
```

## Common mistakes
- Overfitting the public leaderboard.
- Copying notebooks without understanding them.

## Learn more
- [Kaggle competitions](https://www.kaggle.com/competitions) · Free · Practice

## Practice project
Join a "Getting Started" competition and publish your notebook.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
