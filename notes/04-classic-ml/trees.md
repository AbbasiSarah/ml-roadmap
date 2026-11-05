# Trees, forests & boosting

*Classic Machine Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#trees)

> **In one sentence:** Decision trees split data with yes/no questions; forests and boosting combine many trees and win on most table data.

## Key ideas
- A single tree is easy to explain but overfits.
- Random forest = many trees on random samples, averaged: robust with little tuning.
- Gradient boosting (XGBoost, LightGBM, scikit-learn HistGradientBoosting) adds trees that fix previous errors, and is usually the most accurate.
- Trees need no scaling and handle non-linear patterns automatically.
- Feature importance (prefer permutation importance) shows what drives predictions.

## Example
```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
for m in [RandomForestClassifier(300, random_state=0), HistGradientBoostingClassifier(random_state=0)]:
    print(type(m).__name__, cross_val_score(m, X, y, cv=5).mean().round(3))
```

## Common mistakes
- Very deep single trees that memorise the training set.
- Trusting default impurity importance, which is biased towards many-valued features.

## Learn more
- [Kaggle Learn: Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) · Free · Course
- [An Introduction to Statistical Learning (book)](https://www.statlearning.com/) · Free · Book

## Practice project
Compare a decision tree, random forest and gradient boosting on one dataset.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
