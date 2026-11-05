# Python basics

*Python & Tools* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#python-basics)

> **In one sentence:** Python is the language of ML because it is readable and has a library for everything.

## Key ideas
- Core types: `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`.
- Control flow: `if/elif/else`, `for` loops over anything iterable, `while`.
- Functions package logic you reuse; give them clear names and return values.
- List and dict comprehensions replace many loops: `[x**2 for x in nums if x > 0]`.
- Use virtual environments (`python -m venv .venv`) so each project has its own packages.

## Example
```python
expenses = [("food", 1200), ("travel", 800), ("food", 650), ("books", 400)]

totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount

for category, total in sorted(totals.items(), key=lambda kv: -kv[1]):
    print(f"{category:<8} Rs {total:,}")
```

## Common mistakes
- Mutating a list while looping over it.
- Mixing tabs and spaces; use 4 spaces.
- Copy-pasting the same code three times instead of writing a function.

## Learn more
- [Python official tutorial](https://docs.python.org/3/tutorial/) · Free · Docs
- [Kaggle Learn: Python](https://www.kaggle.com/learn/python) · Free · Course

## Practice project
Write a script that reads a CSV of your expenses and prints the total per category.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
