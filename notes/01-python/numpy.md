# NumPy

*Python & Tools* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#numpy)

> **In one sentence:** NumPy stores numbers in fast arrays and does maths on whole arrays at once.

## Key ideas
- An `ndarray` has a `shape` (rows, columns, ...) and a single `dtype`.
- Vectorise: `a * 2` works on every element, no loop needed, and it is about 100× faster.
- Broadcasting lets shapes like (3, 4) and (4,) combine automatically.
- Boolean masks select data: `a[a > 0]`.
- Axis matters: `a.mean(axis=0)` = per column, `axis=1` = per row.

## Example
```python
import numpy as np

scores = np.array([[72, 85, 90], [60, 75, 88], [95, 91, 79]])   # 3 students x 3 exams
print(scores.shape)              # (3, 3)
print(scores.mean(axis=0))       # average per exam
print(scores[scores >= 90])      # all scores of 90+
standardised = (scores - scores.mean(axis=0)) / scores.std(axis=0)
```

## Common mistakes
- Writing Python loops over big arrays instead of vectorising.
- Forgetting that slicing returns a *view*: changing it changes the original. Use `.copy()`.
- Shape mismatches. Print `.shape` whenever something looks wrong.

## Learn more
- [NumPy: learn](https://numpy.org/learn/) · Free · Docs

## Practice project
Re-create a 3×3 image blur using only NumPy array operations.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
