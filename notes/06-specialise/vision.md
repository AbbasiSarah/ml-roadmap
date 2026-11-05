# Computer Vision

*Choose a Specialisation* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#vision)

> **In one sentence:** Computer vision teaches machines to understand images: classify, detect objects, segment pixels.

## Key ideas
- Classification: what is in the image. Detection: where (boxes). Segmentation: which pixels.
- Pretrained backbones (ResNet, ViT) plus fine-tuning work with small datasets.
- Augmentation (flip, crop, colour) is essential.
- Medical and satellite images need careful, expert-checked labels.

## Example
```python
from transformers import pipeline
detector = pipeline("object-detection", model="facebook/detr-resnet-50")
for obj in detector("street.jpg"):
    if obj["score"] > 0.8:
        print(obj["label"], round(obj["score"], 2), obj["box"])
```

## Common mistakes
- Train and test images from the same video or patient (leakage).
- Ignoring class imbalance (few examples of the rare object).

## Learn more
- [Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course) · Free · Course
- [Stanford CS231n notes](https://cs231n.github.io/) · Free · Course

## Practice project
Detect and count objects (e.g. cars) in photos from your city.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
