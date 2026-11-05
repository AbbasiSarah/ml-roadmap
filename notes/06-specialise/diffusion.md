# Image generation

*Choose a Specialisation* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#diffusion)

> **In one sentence:** Diffusion models generate images by starting from noise and removing it step by step, guided by a text prompt.

## Key ideas
- Training: add noise to images, teach a network to predict that noise.
- Generation: start from pure noise and denoise in many small steps.
- Text guidance comes from a text encoder; guidance scale trades creativity for prompt-following.
- Ethics: consent, copyright and deepfakes matter. Label AI-generated images.

## Example
```python
from diffusers import StableDiffusionPipeline
import torch
pipe = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",
                                               torch_dtype=torch.float16).to("cuda")
image = pipe("a watercolour of a robot reading a book in Lahore", num_inference_steps=30).images[0]
image.save("robot.png")
```

## Common mistakes
- Generating real people's likeness without consent.
- Expecting exact text or hands; check outputs carefully.

## Learn more
- [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course) · Free · Course

## Practice project
Generate images in a custom style and explain how diffusion denoises step by step.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
