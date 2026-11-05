"""Stage 2 project: fit a straight line with gradient descent, from scratch, and compare it with the exact answer.

    python gradient_descent.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
hours = rng.uniform(0, 10, 100)                       # hours studied
marks = 35 + 5.5 * hours + rng.normal(0, 5, 100)       # true line: 35 + 5.5x + noise

w, b, lr, losses = 0.0, 0.0, 0.01, []
for step in range(3000):
    pred = w * hours + b
    err = pred - marks
    losses.append((err ** 2).mean())
    w -= lr * 2 * (err * hours).mean()                 # d(MSE)/dw
    b -= lr * 2 * err.mean()                           # d(MSE)/db

exact_w, exact_b = np.polyfit(hours, marks, 1)          # closed-form least squares
print(f"Gradient descent: marks = {b:.2f} + {w:.2f} × hours")
print(f"Exact solution:   marks = {exact_b:.2f} + {exact_w:.2f} × hours")
print(f"Final mean squared error: {losses[-1]:.2f}")

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].scatter(hours, marks, s=12, color="#9fb0d4")
xs = np.linspace(0, 10, 2)
axes[0].plot(xs, b + w * xs, color="#2fe0bf", lw=2.5, label="gradient descent")
axes[0].set(xlabel="Hours studied", ylabel="Marks", title="The learned line"); axes[0].legend(frameon=False)
axes[1].plot(losses, color="#2fe0bf"); axes[1].set(yscale="log", xlabel="Step", ylabel="MSE (log)", title="Loss goes down step by step")
for ax in axes: ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("gradient_descent.png", dpi=130)
