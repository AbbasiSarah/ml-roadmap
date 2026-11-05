"""Stage 5 project: a 2-layer neural network written from scratch in NumPy, learning a curved boundary.

    python neural_net.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

X, y = make_moons(600, noise=0.2, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
ytr = ytr[:, None]

rng = np.random.default_rng(0)
H = 16
W1, b1 = rng.normal(0, 1, (2, H)), np.zeros(H)
W2, b2 = rng.normal(0, 1 / np.sqrt(H), (H, 1)), np.zeros(1)
sigmoid = lambda z: 1 / (1 + np.exp(-z))

def forward(X):
    h = np.tanh(X @ W1 + b1)
    return h, sigmoid(h @ W2 + b2)

lr = 0.5
for epoch in range(2001):
    h, p = forward(Xtr)
    loss = -np.mean(ytr * np.log(p + 1e-9) + (1 - ytr) * np.log(1 - p + 1e-9))
    d_out = (p - ytr) / len(Xtr)                    # gradient at the output (sigmoid + cross-entropy)
    dW2, db2 = h.T @ d_out, d_out.sum(0)
    d_h = (d_out @ W2.T) * (1 - h ** 2)             # backprop through tanh
    dW1, db1 = Xtr.T @ d_h, d_h.sum(0)
    W1 -= lr * dW1; b1 -= lr * db1; W2 -= lr * dW2; b2 -= lr * db2
    if epoch % 500 == 0:
        print(f"epoch {epoch:5d}  loss {loss:.3f}")

acc = ((forward(Xte)[1].ravel() > 0.5) == yte).mean()
print(f"Test accuracy: {acc:.1%}  (a straight-line model gets about 86%)")

xx, yy = np.meshgrid(np.linspace(-1.6, 2.6, 300), np.linspace(-1.1, 1.6, 300))
zz = forward(np.c_[xx.ravel(), yy.ravel()])[1].reshape(xx.shape)
fig, ax = plt.subplots(figsize=(6, 4.2))
ax.contourf(xx, yy, zz, levels=[0, 0.5, 1], colors=["#dfe8fa", "#c9f5ec"])
ax.contour(xx, yy, zz, levels=[0.5], colors="#071433", linewidths=1.5)
ax.scatter(Xte[:, 0], Xte[:, 1], c=yte, cmap="coolwarm", s=14, edgecolor="k", linewidth=0.3)
ax.set(title=f"The network learned a curved boundary ({acc:.0%} on test data)", xticks=[], yticks=[])
plt.tight_layout(); plt.savefig("decision_boundary.png", dpi=130)
