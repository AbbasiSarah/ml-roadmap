"""Generate messy_students.csv with typical real-world problems."""
import numpy as np, pandas as pd
rng = np.random.default_rng(3)
n = 300
cities = rng.choice(["Lahore", "Karachi", "Islamabad", "lhr", " karachi ", "KHI", "Isb", "Karachi."], n)
age = rng.integers(17, 30, n).astype(object)
age[rng.choice(n, 8, replace=False)] = rng.choice([250, -3, 0, 999], 8)
age[rng.choice(n, 12, replace=False)] = None
marks = (rng.normal(68, 12, n).clip(0, 100).round()).astype(int).astype(str)
marks = np.array([m + "%" if rng.random() < 0.2 else m for m in marks], dtype=object)
marks[rng.choice(n, 15, replace=False)] = rng.choice(["", "absent", "n/a"], 15)
df = pd.DataFrame({"student_id": np.arange(1, n + 1), "city": cities, "age": age, "marks": marks})
df = pd.concat([df, df.sample(20, random_state=1)])        # duplicates
df.to_csv("messy_students.csv", index=False)
print("messy_students.csv:", len(df), "rows")
