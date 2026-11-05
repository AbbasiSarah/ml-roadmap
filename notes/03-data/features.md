# Feature engineering

*Data Skills* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#features)

> **In one sentence:** Feature engineering turns raw columns into signals a model can learn from.

## Key ideas
- Ratios often beat raw totals (rooms per household vs total rooms).
- Dates → day of week, month, holiday flags.
- Categories → one-hot encoding; many categories → target or frequency encoding (inside CV!).
- Scale numeric features for linear models and neural networks; trees don't need it.
- Put all steps in a scikit-learn `Pipeline` so they are learned on training data only.

## Example
```python
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

prep = make_column_transformer((StandardScaler(), ["age", "income"]),
                               (OneHotEncoder(handle_unknown="ignore"), ["city"]))
model = make_pipeline(prep, LogisticRegression())
```

## Common mistakes
- Engineering features using the test set.
- Adding hundreds of features without checking whether they help.

## Learn more
- [Kaggle Learn: Feature Engineering](https://www.kaggle.com/learn/feature-engineering) · Free · Course

## Practice project
Add three engineered features to a dataset and measure whether the model improves.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
