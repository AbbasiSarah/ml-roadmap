# Neural networks & backpropagation

*Deep Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#neural-nets)

> **In one sentence:** A neural network is layers of weighted sums plus non-linear activations, trained by sending the error backwards (backpropagation).

## Key ideas
- Neuron: output = activation(w · x + b). ReLU is the default activation.
- Loss measures error: MSE for numbers, cross-entropy for classes.
- Backpropagation = chain rule; it gives the gradient for every weight.
- Optimisers (SGD, Adam) update weights with those gradients.
- Overfitting fixes: more data, dropout, weight decay, early stopping.

## Example
```python
import numpy as np
X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])     # XOR inputs + a constant 1 (bias)
y = np.array([[0],[1],[1],[0]])
rng = np.random.default_rng(0); W1, W2 = rng.normal(size=(3, 8)), rng.normal(size=(8, 1))
sig = lambda z: 1 / (1 + np.exp(-z))
for _ in range(5000):
    h = np.tanh(X @ W1); p = sig(h @ W2)
    d2 = p - y                          # gradient of cross-entropy wrt logits
    W2 -= 0.1 * h.T @ d2
    W1 -= 0.1 * X.T @ ((d2 @ W2.T) * (1 - h**2))
print(p.round(2).ravel())               # ~[0, 1, 1, 0]
```

## Common mistakes
- Not normalising inputs.
- Judging training only by training loss; watch validation loss.

## Learn more
- [3Blue1Brown: Neural networks](https://www.3blue1brown.com/topics/neural-networks) · Free · Video
- [Andrej Karpathy: Neural Networks, Zero to Hero](https://karpathy.ai/zero-to-hero.html) · Free · Video

## Practice project
Build a tiny neural network from scratch in NumPy that learns XOR.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
