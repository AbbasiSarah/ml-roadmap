# Linear algebra

*Math for ML* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#linear-algebra)

> **In one sentence:** Data is a matrix and every model layer is a matrix multiplication, so linear algebra is the grammar of ML.

## Key ideas
- A vector is a list of numbers (one data point); a matrix is a table (many points).
- Dot product measures similarity: it is the heart of recommendation, search and attention.
- Matrix multiplication `X @ W` transforms every row of data at once.
- Shapes must line up: (n, d) @ (d, k) → (n, k).
- Eigenvectors and PCA find the directions where data varies most.

## Example
```python
import numpy as np

X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])   # 3 points, 2 features
W = np.array([[0.5], [-1.0]])                        # weights: 2 -> 1
print(X @ W)                                         # one prediction per point

a, b = np.array([1, 2, 3]), np.array([2, 4, 6])
cosine = a @ b / (np.linalg.norm(a) * np.linalg.norm(b))
print(round(cosine, 3))                              # 1.0 = same direction
```

## Common mistakes
- Confusing element-wise `*` with matrix multiplication `@`.
- Memorising formulas without the picture. Watch 3Blue1Brown first.
- Ignoring shapes: write them in comments while you code.

## Learn more
- [3Blue1Brown: Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra) · Free · Video
- [Mathematics for Machine Learning (book)](https://mml-book.github.io/) · Free · Book

## Practice project
Implement matrix multiplication with plain loops, then check it against NumPy.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
