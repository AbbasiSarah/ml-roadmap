"""Stage 3 project: clean a messy dataset and log every change.

    python clean.py        # reads messy_students.csv, writes clean_students.csv + cleaning_log.txt
"""
import numpy as np
import pandas as pd

df = pd.read_csv("messy_students.csv")
log = [f"Loaded {len(df)} rows, {df.shape[1]} columns"]

n = len(df); df = df.drop_duplicates(); log.append(f"Removed {n - len(df)} exact duplicate rows")

df["city"] = df["city"].str.strip().str.title()
fix = {"Lhr": "Lahore", "Khi": "Karachi", "Isb": "Islamabad", "Karachi.": "Karachi"}
log.append(f"Standardised city names ({df['city'].isin(fix).sum()} abbreviations fixed)")
df["city"] = df["city"].replace(fix)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
bad_age = (~df["age"].between(15, 70)) & df["age"].notna()
log.append(f"Set {bad_age.sum()} impossible ages to missing")
df.loc[bad_age, "age"] = np.nan

df["marks"] = pd.to_numeric(df["marks"].astype(str).str.replace("%", ""), errors="coerce")
log.append(f"Converted marks to numbers ({df['marks'].isna().sum()} missing)")

for col in ["age", "marks"]:
    df[f"{col}_was_missing"] = df[col].isna().astype(int)
    med = df[col].median()
    log.append(f"Filled {df[col].isna().sum()} missing {col} with median {med:.0f} (flag column added)")
    df[col] = df[col].fillna(med)

df.to_csv("clean_students.csv", index=False)
log.append(f"Saved {len(df)} clean rows")
open("cleaning_log.txt", "w").write("\n".join(log) + "\n")
print("\n".join(log))
