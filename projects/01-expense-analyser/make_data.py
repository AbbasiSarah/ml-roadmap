"""Create a sample expenses.csv (one year of made-up household spending)."""
import numpy as np, pandas as pd
rng = np.random.default_rng(7)
cats = {"Groceries": 9000, "Transport": 4500, "Bills": 7000, "Eating out": 3000, "Education": 6000, "Shopping": 4000}
rows = []
for day in pd.date_range("2026-01-01", "2026-12-31"):
    for c, monthly in cats.items():
        if rng.random() < 0.18:
            rows.append((day.date(), c, round(rng.gamma(2, monthly / 10), -1)))
pd.DataFrame(rows, columns=["date", "category", "amount"]).to_csv("expenses.csv", index=False)
print(len(rows), "expenses written")
