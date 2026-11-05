# Time Series & Forecasting

*Choose a Specialisation* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#time-series)

> **In one sentence:** Time-series forecasting predicts the future from the past: sales, demand, weather, health signals.

## Key ideas
- Look for trend, seasonality (weekly, yearly) and holidays.
- Always beat a naive baseline: "tomorrow = today" or "same week last year".
- Split by time: train on the past, test on the future (rolling-origin evaluation).
- Lag features (yesterday, last week) let ordinary ML models forecast.
- Report error in units people understand (e.g. ±120 units, MAPE).

## Example
```python
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
s = pd.read_csv("sales.csv", parse_dates=["date"], index_col="date")["sales"]
df = pd.DataFrame({"y": s, "lag1": s.shift(1), "lag7": s.shift(7), "dow": s.index.dayofweek}).dropna()
train, test = df[:-30], df[-30:]                       # last 30 days = future
m = HistGradientBoostingRegressor().fit(train.drop(columns="y"), train.y)
print("MAE:", (m.predict(test.drop(columns="y")) - test.y).abs().mean())
```

## Common mistakes
- Random shuffling of time-series data.
- Not comparing with a naive baseline.

## Learn more
- [Forecasting: Principles and Practice (book)](https://otexts.com/fpp3/) · Free · Book
- [Kaggle Learn: Time Series](https://www.kaggle.com/learn/time-series) · Free · Course

## Practice project
Forecast next month's sales; or see my health research: depression detection from activity data.

Example: https://abbasisarah.github.io/depression-bipolar_CNN/

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
