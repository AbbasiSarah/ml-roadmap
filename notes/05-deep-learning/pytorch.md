# PyTorch

*Deep Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#pytorch)

> **In one sentence:** PyTorch builds and trains neural networks with automatic gradients and GPU support. It is the standard in research and industry.

## Key ideas
- Tensors are NumPy arrays that can live on a GPU and track gradients.
- `nn.Module` defines a model; `forward` describes the computation.
- Training loop: forward → loss → `loss.backward()` → `optimizer.step()` → `optimizer.zero_grad()`.
- `model.train()` vs `model.eval()` changes dropout and batch norm behaviour.
- `DataLoader` handles batching and shuffling.

## Example
```python
import torch, torch.nn as nn
model = nn.Sequential(nn.Linear(10, 32), nn.ReLU(), nn.Linear(32, 2))
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()
for xb, yb in loader:                   # loader = DataLoader(dataset, batch_size=64, shuffle=True)
    loss = loss_fn(model(xb), yb)
    opt.zero_grad(); loss.backward(); opt.step()
```

## Common mistakes
- Forgetting `zero_grad()`, so gradients pile up.
- Evaluating without `torch.no_grad()` and `model.eval()`.

## Learn more
- [PyTorch tutorials](https://pytorch.org/tutorials/) · Free · Docs
- [fast.ai: Practical Deep Learning](https://course.fast.ai/) · Free · Course

## Practice project
Train an image classifier on your own photos with PyTorch.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
