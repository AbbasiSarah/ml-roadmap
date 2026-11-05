# CNNs for images

*Deep Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#cnn)

> **In one sentence:** Convolutional networks slide small filters over images to detect edges, then shapes, then objects.

## Key ideas
- A convolution filter (e.g. 3×3) shares its weights across the whole image, so it needs far fewer parameters than a dense layer.
- Pooling shrinks the image and adds tolerance to small shifts.
- Deeper layers see larger areas and more abstract features.
- Transfer learning: start from a network pretrained on millions of images and fine-tune it on yours.

## Example
```python
import torch.nn as nn
cnn = nn.Sequential(
    nn.Conv2d(1, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),    # 28 -> 14
    nn.Conv2d(8, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),   # 14 -> 7
    nn.Flatten(), nn.Linear(16 * 7 * 7, 64), nn.ReLU(), nn.Linear(64, 10))
```

## Common mistakes
- Training from scratch on a few hundred images; use transfer learning.
- No data augmentation (flips, shifts, crops).

## Learn more
- [Dive into Deep Learning (book)](https://d2l.ai/) · Free · Book
- [Stanford CS231n notes](https://cs231n.github.io/) · Free · Course

## Practice project
Handwritten digit recognition with a live demo; see my example: Digit CNN.

Example: https://abbasisarah.github.io/handwritten-digit-cnn/

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
