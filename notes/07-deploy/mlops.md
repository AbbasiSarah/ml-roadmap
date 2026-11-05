# MLOps

*Deploy & MLOps* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#mlops)

> **In one sentence:** MLOps keeps models reliable after launch: tracking experiments, versioning data, retraining and monitoring.

## Key ideas
- Track every experiment: data version, parameters, metrics (MLflow, Weights & Biases).
- Automate: tests and retraining pipelines (GitHub Actions, Airflow).
- Monitor data drift: when real inputs change, accuracy silently drops.
- Keep a model card: what it's for, data, metrics, limitations.

## Example
```python
import mlflow
with mlflow.start_run():
    mlflow.log_param("model", "random_forest"); mlflow.log_param("n_estimators", 300)
    mlflow.log_metric("val_auc", 0.91)
    mlflow.sklearn.log_model(model, "model")
```

## Common mistakes
- "Final_model_v7_really_final.pkl" with no record of how it was made.
- Never checking a deployed model's accuracy again.

## Learn more
- [Made With ML](https://madewithml.com/) · Free · Course
- [DataTalksClub MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) · Free · Course

## Practice project
Retrain a model automatically each week and log every run's accuracy.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
