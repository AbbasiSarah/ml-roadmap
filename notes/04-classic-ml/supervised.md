# Regression & classification

*Classic Machine Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#supervised)

> **In one sentence:** Supervised learning learns from examples with known answers to predict a number (regression) or a category (classification).

## Key ideas
- Split data: train to learn, validation to choose, test to report, used once.
- Start with a baseline (predict the average or the most common class) so you know what "good" means.
- Linear and logistic regression are fast, explainable starting points.
- Regression metrics: MAE, RMSE, R². Classification: accuracy, precision, recall, F1, ROC-AUC.

## Example
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)
print("test accuracy:", model.score(Xte, yte))
```

## Common mistakes
- Reporting training accuracy as the result.
- Using accuracy on imbalanced data (99% "not spam" is useless).

## Learn more
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) · Free · Course
- [Andrew Ng: Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) · Paid · Course
- [Kaggle Learn: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) · Free · Course

## Practice project
Predict house prices; see my example: California House Prices.

Example: https://github.com/AbbasiSarah/california-house-prices

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
