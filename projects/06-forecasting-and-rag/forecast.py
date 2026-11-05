"""Stage 6 project (time-series track): forecast 60 days of daily sales and beat the naive baselines.

    python forecast.py

The data is simulated: a growing shop with a weekly rhythm (Fri/Sat busiest), a yearly season and Eid peaks.
The model uses only things known in advance (the date, the calendar, the holidays), so it can forecast
weeks ahead, unlike "same as last week".
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge

rng = np.random.default_rng(1)
days = pd.date_range("2024-01-01", "2026-10-31")
EID = ["2024-04-10", "2024-04-11", "2024-06-16", "2024-06-17", "2025-03-30", "2025-03-31",
       "2025-06-06", "2025-06-07", "2026-03-20", "2026-03-21", "2026-05-27", "2026-05-28"]
t = np.arange(len(days))
weekly = np.array([0.85, 0.9, 0.95, 1.0, 1.25, 1.35, 1.1])[days.dayofweek]
yearly = 1 + 0.15 * np.sin(2 * np.pi * (days.dayofyear - 80) / 365)
eid = days.isin(pd.to_datetime(EID))
sales = pd.Series((200 + 0.08 * t) * weekly * yearly * (1 + 0.6 * eid) + rng.normal(0, 12, len(t)), index=days).round()


def calendar_features(idx, t):
    X = pd.get_dummies(idx.dayofweek, prefix="dow", dtype=float)
    X.index = idx
    for k in (1, 2):                                       # smooth yearly season (Fourier terms)
        X[f"sin{k}"] = np.sin(2 * np.pi * k * idx.dayofyear / 365.25)
        X[f"cos{k}"] = np.cos(2 * np.pi * k * idx.dayofyear / 365.25)
    X["trend"] = t / 365
    X["eid"] = idx.isin(pd.to_datetime(EID)).astype(float)
    return X


H = 60                                                     # forecast horizon (days)
X = calendar_features(days, t)
Xtr, Xte, ytr, yte = X.iloc[:-H], X.iloc[-H:], sales.iloc[:-H], sales.iloc[-H:]
model = Ridge(alpha=1.0).fit(Xtr, np.log(ytr))             # log: effects multiply, like real sales
pred = pd.Series(np.exp(model.predict(Xte)), index=yte.index)

naive7 = sales.shift(7).iloc[-H:]                          # needs last week's actuals (only 7 days ahead)
naive364 = sales.shift(364).iloc[-H:]
mae = lambda p: (p - yte).abs().mean()
results = {"Naive: same as 7 days ago": mae(naive7),
           "Naive: same weekday last year": mae(naive364),
           "Regression on calendar features": mae(pred)}
for k, v in results.items():
    print(f"{k:<34} MAE {v:6.1f} units/day")
gain = 1 - results["Regression on calendar features"] / results["Naive: same as 7 days ago"]
print(f"\nThe model's error is {abs(gain):.0%} {'lower' if gain > 0 else 'higher'} than the best naive forecast,")
print("and it can forecast all 60 days at once, while 'same as 7 days ago' only works one week ahead.")

fig, ax = plt.subplots(figsize=(10, 3.8))
ax.plot(sales.index[-150:], sales.values[-150:], color="#9fb0d4", lw=1, label="actual")
ax.plot(pred.index, pred.values, color="#2fe0bf", lw=2, label="60-day forecast")
ax.axvline(yte.index[0], color="#071433", ls=":", lw=1)
ax.set(title=f"60-day forecast: {abs(gain):.0%} lower error than 'same as last week'", ylabel="Units sold")
ax.legend(frameon=False); ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("forecast.png", dpi=130)
