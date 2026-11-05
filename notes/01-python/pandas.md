# Pandas

*Python & Tools* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#pandas)

> **In one sentence:** Pandas is Excel inside Python: tables (DataFrames) you can filter, group and join with code.

## Key ideas
- `pd.read_csv()` loads a file; `df.head()`, `df.info()`, `df.describe()` give a first look.
- Select columns with `df['col']`, rows with `df[df.age > 30]` or `df.loc[...]`.
- `groupby` + `agg` answers "per category" questions in one line.
- `merge` joins two tables on a key column, like SQL JOIN.
- Missing values: `df.isna().sum()`, then `fillna` or `dropna` on purpose, not by habit.

## Example
```python
import pandas as pd

df = pd.DataFrame({"city": ["Karachi", "Lahore", "Karachi", "Islamabad"],
                   "sales": [120, 90, 150, 70]})
summary = df.groupby("city")["sales"].agg(["count", "sum", "mean"])
print(summary.sort_values("sum", ascending=False))
```

## Common mistakes
- Chained indexing (`df[a][b] = x`) that silently doesn't change the data. Use `.loc`.
- Looping over rows with `iterrows()` when a vectorised column operation exists.
- Not checking `dtypes`: numbers stored as text break calculations.

## Learn more
- [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas) · Free · Course
- [pandas getting started](https://pandas.pydata.org/docs/getting_started/index.html) · Free · Docs

## Practice project
Analyse a public dataset (e.g. cricket or weather) and answer three questions with group-by tables.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
