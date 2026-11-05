"""Stage 4 project: compare classic ML models honestly on breast-cancer diagnosis data.

    python compare_models.py
Uses scikit-learn's built-in Wisconsin breast cancer dataset (569 tumours, 30 measurements).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, recall_score
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

data = load_breast_cancer()
X, y = data.data, 1 - data.target            # 1 = malignant (the case we must not miss)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

models = {
    "Baseline (always benign)": DummyClassifier(strategy="most_frequent"),
    "Logistic regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
    "Decision tree": DecisionTreeClassifier(max_depth=4, random_state=0),
    "Random forest": RandomForestClassifier(300, random_state=0),
    "Gradient boosting": HistGradientBoostingClassifier(random_state=0),
}
cv = StratifiedKFold(5, shuffle=True, random_state=0)
print(f"{'Model':<26}{'CV accuracy':>12}{'CV recall':>11}{'CV ROC-AUC':>12}")
rows = {}
for name, m in models.items():
    s = cross_validate(m, Xtr, ytr, cv=cv, scoring=["accuracy", "recall", "roc_auc"])
    rows[name] = {k: s[f"test_{k}"].mean() for k in ["accuracy", "recall", "roc_auc"]}
    print(f"{name:<26}{rows[name]['accuracy']:>12.3f}{rows[name]['recall']:>11.3f}{rows[name]['roc_auc']:>12.3f}")

best = max((n for n in rows if not n.startswith("Baseline")), key=lambda n: rows[n]["roc_auc"])
final = models[best].fit(Xtr, ytr)
pred = final.predict(Xte)
cm = confusion_matrix(yte, pred)
print(f"\nChosen on cross-validation: {best}")
print(f"Held-out test: accuracy {(pred == yte).mean():.3f}, malignant tumours caught {recall_score(yte, pred):.1%}")
print(f"Missed cancers (false negatives): {cm[1, 0]}   False alarms: {cm[0, 1]}")
print("\nNote: the baseline scores ~63% accuracy while catching 0% of cancers. Accuracy alone can mislead.")

names = list(rows)
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.barh(names[::-1], [rows[n]["roc_auc"] for n in names[::-1]],
        color=["#2fe0bf" if n == best else "#9fb0d4" for n in names[::-1]])
ax.set(xlim=(0.4, 1.0), xlabel="ROC-AUC (5-fold CV)", title=f"{best} separates tumours best")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("model_comparison.png", dpi=130)
