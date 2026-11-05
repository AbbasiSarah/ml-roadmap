# Evaluation & avoiding leakage

*Classic Machine Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#evaluation)

> **In one sentence:** Honest evaluation means testing on data the model truly never saw. It separates real results from fake 99% accuracy.

## Key ideas
- Cross-validation averages several train/test splits for a stable estimate.
- Group splits: if one person or place has many rows, keep all of them on the same side (`GroupKFold`).
- Time series: always train on the past and test on the future.
- Leakage = information from the test set or the future reaching training (duplicates, scaling on all data, target-derived features).
- Pick metrics for the cost of mistakes: missed cancer ≠ false alarm.

## Example
```python
from sklearn.model_selection import GroupKFold, cross_val_score
# rows from the same patient must not be in both train and test
scores = cross_val_score(model, X, y, groups=patient_id, cv=GroupKFold(5), scoring="roc_auc")
print(scores.mean(), scores.std())
```

## Common mistakes
- Random splits on data with repeated people, days or places.
- Tuning on the test set; it is then no longer a test.
- Not removing duplicate rows before splitting.

## Learn more
- [scikit-learn: model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) · Free · Docs
- [Kaggle Learn: Intermediate ML (data leakage)](https://www.kaggle.com/learn/intermediate-machine-learning) · Free · Course

## Practice project
Build a spam filter and report precision, recall and false alarms; see my example: SMS Spam Classifier.

Example: https://github.com/AbbasiSarah/sms-spam-classifier

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
