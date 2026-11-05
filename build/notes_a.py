NOTES = {}

NOTES["python-basics"] = dict(
    one="Python is the language of ML because it is readable and has a library for everything.",
    ideas=["Core types: `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`.",
           "Control flow: `if/elif/else`, `for` loops over anything iterable, `while`.",
           "Functions package logic you reuse; give them clear names and return values.",
           "List and dict comprehensions replace many loops: `[x**2 for x in nums if x > 0]`.",
           "Use virtual environments (`python -m venv .venv`) so each project has its own packages."],
    code='''expenses = [("food", 1200), ("travel", 800), ("food", 650), ("books", 400)]

totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount

for category, total in sorted(totals.items(), key=lambda kv: -kv[1]):
    print(f"{category:<8} Rs {total:,}")''',
    mistakes=["Mutating a list while looping over it.",
              "Mixing tabs and spaces; use 4 spaces.",
              "Copy-pasting the same code three times instead of writing a function."])

NOTES["numpy"] = dict(
    one="NumPy stores numbers in fast arrays and does maths on whole arrays at once.",
    ideas=["An `ndarray` has a `shape` (rows, columns, ...) and a single `dtype`.",
           "Vectorise: `a * 2` works on every element, no loop needed, and it is about 100× faster.",
           "Broadcasting lets shapes like (3, 4) and (4,) combine automatically.",
           "Boolean masks select data: `a[a > 0]`.",
           "Axis matters: `a.mean(axis=0)` = per column, `axis=1` = per row."],
    code='''import numpy as np

scores = np.array([[72, 85, 90], [60, 75, 88], [95, 91, 79]])   # 3 students x 3 exams
print(scores.shape)              # (3, 3)
print(scores.mean(axis=0))       # average per exam
print(scores[scores >= 90])      # all scores of 90+
standardised = (scores - scores.mean(axis=0)) / scores.std(axis=0)''',
    mistakes=["Writing Python loops over big arrays instead of vectorising.",
              "Forgetting that slicing returns a *view*: changing it changes the original. Use `.copy()`.",
              "Shape mismatches. Print `.shape` whenever something looks wrong."])

NOTES["pandas"] = dict(
    one="Pandas is Excel inside Python: tables (DataFrames) you can filter, group and join with code.",
    ideas=["`pd.read_csv()` loads a file; `df.head()`, `df.info()`, `df.describe()` give a first look.",
           "Select columns with `df['col']`, rows with `df[df.age > 30]` or `df.loc[...]`.",
           "`groupby` + `agg` answers \"per category\" questions in one line.",
           "`merge` joins two tables on a key column, like SQL JOIN.",
           "Missing values: `df.isna().sum()`, then `fillna` or `dropna` on purpose, not by habit."],
    code='''import pandas as pd

df = pd.DataFrame({"city": ["Karachi", "Lahore", "Karachi", "Islamabad"],
                   "sales": [120, 90, 150, 70]})
summary = df.groupby("city")["sales"].agg(["count", "sum", "mean"])
print(summary.sort_values("sum", ascending=False))''',
    mistakes=["Chained indexing (`df[a][b] = x`) that silently doesn't change the data. Use `.loc`.",
              "Looping over rows with `iterrows()` when a vectorised column operation exists.",
              "Not checking `dtypes`: numbers stored as text break calculations."])

NOTES["visualisation"] = dict(
    one="A good chart answers one question at a glance; its title states the finding.",
    ideas=["Pick the chart from the question: trend → line, compare categories → bar, relationship → scatter, distribution → histogram.",
           "One accent colour for what matters; everything else grey.",
           "Label axes with units; start bar axes at zero.",
           "Seaborn makes statistical plots (box plots, heatmaps) in one line on top of Matplotlib."],
    code='''import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
signups = [120, 135, 160, 210, 260]
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(months, signups, marker="o", color="#2fe0bf", lw=2.5)
ax.set(title="Sign-ups more than doubled from January to May", ylabel="Sign-ups per month")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("signups.png", dpi=150)''',
    mistakes=["Pie charts with many slices: use a sorted bar chart.",
              "Rainbow colours that carry no meaning.",
              "A title that only names the chart (\"Sales\") instead of saying what it shows."])

NOTES["git"] = dict(
    one="Git saves every version of your code; GitHub puts it online, which makes it your public portfolio.",
    ideas=["Core loop: `git add` → `git commit -m \"message\"` → `git push`.",
           "Commit small, meaningful changes with messages that say *why*.",
           "`.gitignore` keeps junk (data caches, `.venv`, secrets) out of the repository.",
           "A clear README (what, results, how to run) matters more than the code for recruiters.",
           "Never commit passwords or API keys. Once pushed, assume they are public forever."],
    code='''git init
git add analysis.py README.md
git commit -m "Add first expense analysis"
git branch -M main
git remote add origin https://github.com/<you>/expense-analysis.git
git push -u origin main''',
    mistakes=["Committing large datasets or model files (use links or Git LFS).",
              "Messages like \"update\" or \"final final v2\".",
              "Pushing secrets. Rotate the key immediately if it happens."])

NOTES["linear-algebra"] = dict(
    one="Data is a matrix and every model layer is a matrix multiplication, so linear algebra is the grammar of ML.",
    ideas=["A vector is a list of numbers (one data point); a matrix is a table (many points).",
           "Dot product measures similarity: it is the heart of recommendation, search and attention.",
           "Matrix multiplication `X @ W` transforms every row of data at once.",
           "Shapes must line up: (n, d) @ (d, k) → (n, k).",
           "Eigenvectors and PCA find the directions where data varies most."],
    code='''import numpy as np

X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])   # 3 points, 2 features
W = np.array([[0.5], [-1.0]])                        # weights: 2 -> 1
print(X @ W)                                         # one prediction per point

a, b = np.array([1, 2, 3]), np.array([2, 4, 6])
cosine = a @ b / (np.linalg.norm(a) * np.linalg.norm(b))
print(round(cosine, 3))                              # 1.0 = same direction''',
    mistakes=["Confusing element-wise `*` with matrix multiplication `@`.",
              "Memorising formulas without the picture. Watch 3Blue1Brown first.",
              "Ignoring shapes: write them in comments while you code."])

NOTES["calculus"] = dict(
    one="A derivative says which way is downhill, and gradient descent walks downhill on the error until the model is good.",
    ideas=["The derivative of a loss with respect to a weight tells how the loss changes if the weight moves a little.",
           "Gradient = all those derivatives together, pointing uphill; we step the opposite way.",
           "Learning rate = step size: too big jumps around, too small takes forever.",
           "The chain rule is backpropagation: gradients flow backwards through layers."],
    code='''# minimise f(x) = (x - 3)^2 with gradient descent
x, lr = 0.0, 0.1
for step in range(25):
    grad = 2 * (x - 3)        # derivative of (x-3)^2
    x -= lr * grad
print(round(x, 4))           # ~3.0''',
    mistakes=["A learning rate so high the loss explodes. Try 10× smaller.",
              "Thinking you must do calculus by hand; libraries do it, but you must understand it."])

NOTES["stats"] = dict(
    one="Statistics tells you how sure you can be: whether a pattern is real or just noise.",
    ideas=["Describe data: mean vs median (robust to outliers), standard deviation, percentiles.",
           "Distributions: normal, binomial, Poisson; know when each appears.",
           "Correlation ≠ causation; a third factor often explains both.",
           "Sampling and confidence intervals: a result from 30 people is less certain than from 3,000.",
           "Hypothesis tests and p-values answer \"could this happen by chance?\""],
    code='''import numpy as np
rng = np.random.default_rng(0)
flips = rng.integers(0, 2, size=10_000)
running = flips.cumsum() / np.arange(1, len(flips) + 1)
print(running[[9, 99, 999, 9999]])     # approaches 0.5: law of large numbers''',
    mistakes=["Reporting accuracy without uncertainty on tiny datasets.",
              "Using the mean on very skewed data (incomes, prices); show the median too.",
              "P-hacking: testing many things until one looks significant."])

NOTES["cleaning"] = dict(
    one="Most ML time is spent cleaning data, and a model is only as good as its data.",
    ideas=["Check: missing values, duplicates, wrong types, impossible values (age 250), inconsistent labels (\"Lhr\" vs \"Lahore\").",
           "Decide per column: drop, fill (median/most frequent), or flag as a feature (\"was missing\").",
           "Remove exact duplicates *before* splitting train/test, or the test set leaks.",
           "Keep a log of every change, so others can trust your result."],
    code='''import pandas as pd
df = pd.read_csv("messy.csv")
df = df.drop_duplicates()
df["city"] = df["city"].str.strip().str.title().replace({"Lhr": "Lahore"})
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df.loc[~df["age"].between(0, 110), "age"] = None
df["age"] = df["age"].fillna(df["age"].median())''',
    mistakes=["Filling missing values using statistics from the *whole* dataset, test rows included (leakage).",
              "Silently dropping rows without counting how many.",
              "Fixing data by hand in Excel, so nobody can repeat it."])

NOTES["eda"] = dict(
    one="Exploratory data analysis means looking before you model: find patterns, problems and surprises.",
    ideas=["Start with shape, types, missing values and target balance.",
           "Plot every important column's distribution, then the target against each feature.",
           "Look for leakage: a feature that is suspiciously perfect usually contains the answer.",
           "Write findings as sentences; each should change what you do next."],
    code='''import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
df = sns.load_dataset("tips")
print(df.describe(include="all").T)
sns.boxplot(data=df, x="day", y="tip"); plt.title("Tips are highest on Sundays"); plt.show()''',
    mistakes=["Skipping EDA and going straight to models.",
              "Making 50 charts and no conclusions."])

NOTES["features"] = dict(
    one="Feature engineering turns raw columns into signals a model can learn from.",
    ideas=["Ratios often beat raw totals (rooms per household vs total rooms).",
           "Dates → day of week, month, holiday flags.",
           "Categories → one-hot encoding; many categories → target or frequency encoding (inside CV!).",
           "Scale numeric features for linear models and neural networks; trees don't need it.",
           "Put all steps in a scikit-learn `Pipeline` so they are learned on training data only."],
    code='''from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

prep = make_column_transformer((StandardScaler(), ["age", "income"]),
                               (OneHotEncoder(handle_unknown="ignore"), ["city"]))
model = make_pipeline(prep, LogisticRegression())''',
    mistakes=["Engineering features using the test set.",
              "Adding hundreds of features without checking whether they help."])

NOTES["sql"] = dict(
    one="SQL is how you ask a database questions, and in most jobs it is how you get the data in the first place.",
    ideas=["`SELECT ... FROM ... WHERE ...` filters rows.",
           "`GROUP BY` with `COUNT`, `SUM`, `AVG` summarises.",
           "`JOIN` combines tables on a key.",
           "Window functions (`ROW_NUMBER() OVER (...)`) answer \"top N per group\" questions."],
    code='''SELECT city,
       COUNT(*)          AS orders,
       ROUND(AVG(total)) AS avg_order
FROM orders
WHERE order_date >= '2026-01-01'
GROUP BY city
ORDER BY orders DESC
LIMIT 5;''',
    mistakes=["`SELECT *` on huge tables.",
              "Joins that multiply rows by accident; check row counts before and after."])
