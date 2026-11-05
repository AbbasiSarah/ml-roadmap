"""Stage 1 project: where does the money go? (Python, Pandas, Matplotlib)

    python make_data.py      # creates expenses.csv (or use your own: date,category,amount)
    python analyse.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("expenses.csv", parse_dates=["date"])
total = df.amount.sum()
by_cat = df.groupby("category").amount.sum().sort_values(ascending=False)
by_month = df.groupby(df.date.dt.to_period("M")).amount.sum()

print(f"Total spent: Rs {total:,.0f} across {len(df)} payments\n")
for cat, amt in by_cat.items():
    print(f"{cat:<12} Rs {amt:>10,.0f}  {amt / total:5.1%}")
print(f"\nMost expensive month: {by_month.idxmax()} (Rs {by_month.max():,.0f})")

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
colors = ["#2fe0bf"] + ["#9fb0d4"] * (len(by_cat) - 1)
axes[0].barh(by_cat.index[::-1], by_cat.values[::-1] / 1000, color=colors[::-1])
axes[0].set(title=f"{by_cat.index[0]} is the biggest expense", xlabel="Rs thousand")
axes[1].plot(by_month.index.astype(str), by_month.values / 1000, marker="o", color="#2fe0bf")
axes[1].set(title="Spending per month", ylabel="Rs thousand"); axes[1].tick_params(axis="x", rotation=45)
for ax in axes: ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("spending.png", dpi=130)
print("Chart saved to spending.png")
