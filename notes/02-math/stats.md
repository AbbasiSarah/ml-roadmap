# Probability & statistics

*Math for ML* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#stats)

> **In one sentence:** Statistics tells you how sure you can be: whether a pattern is real or just noise.

## Key ideas
- Describe data: mean vs median (robust to outliers), standard deviation, percentiles.
- Distributions: normal, binomial, Poisson; know when each appears.
- Correlation ≠ causation; a third factor often explains both.
- Sampling and confidence intervals: a result from 30 people is less certain than from 3,000.
- Hypothesis tests and p-values answer "could this happen by chance?"

## Example
```python
import numpy as np
rng = np.random.default_rng(0)
flips = rng.integers(0, 2, size=10_000)
running = flips.cumsum() / np.arange(1, len(flips) + 1)
print(running[[9, 99, 999, 9999]])     # approaches 0.5: law of large numbers
```

## Common mistakes
- Reporting accuracy without uncertainty on tiny datasets.
- Using the mean on very skewed data (incomes, prices); show the median too.
- P-hacking: testing many things until one looks significant.

## Learn more
- [Khan Academy: Statistics & probability](https://www.khanacademy.org/math/statistics-probability) · Free · Course
- [StatQuest (Josh Starmer)](https://statquest.org/) · Free · Video

## Practice project
Simulate 10,000 coin flips and show the law of large numbers in a chart.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
