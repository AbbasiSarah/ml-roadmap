# Data visualisation

*Python & Tools* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#visualisation)

> **In one sentence:** A good chart answers one question at a glance; its title states the finding.

## Key ideas
- Pick the chart from the question: trend → line, compare categories → bar, relationship → scatter, distribution → histogram.
- One accent colour for what matters; everything else grey.
- Label axes with units; start bar axes at zero.
- Seaborn makes statistical plots (box plots, heatmaps) in one line on top of Matplotlib.

## Example
```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
signups = [120, 135, 160, 210, 260]
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(months, signups, marker="o", color="#2fe0bf", lw=2.5)
ax.set(title="Sign-ups more than doubled from January to May", ylabel="Sign-ups per month")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("signups.png", dpi=150)
```

## Common mistakes
- Pie charts with many slices: use a sorted bar chart.
- Rainbow colours that carry no meaning.
- A title that only names the chart ("Sales") instead of saying what it shows.

## Learn more
- [Kaggle Learn: Data Visualization](https://www.kaggle.com/learn/data-visualization) · Free · Course

## Practice project
Make one clear chart that answers one question, with a title that states the finding.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
