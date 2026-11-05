# Transformers & attention

*Deep Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#transformers)

> **In one sentence:** Transformers use attention to let every word look at every other word. This architecture powers ChatGPT and most modern AI.

## Key ideas
- Text is split into tokens and turned into vectors (embeddings).
- Self-attention: each token scores how relevant every other token is (a dot product), then mixes their information.
- Positional encodings tell the model the word order.
- Pretrain on huge text by predicting the next token; then fine-tune or prompt for tasks.
- Encoder models (BERT) suit classification; decoder models (GPT) generate text.

## Example
```python
import numpy as np
def attention(Q, K, V):
    scores = Q @ K.T / np.sqrt(K.shape[1])            # how much each token attends to each other
    w = np.exp(scores - scores.max(1, keepdims=True))
    w /= w.sum(1, keepdims=True)                      # softmax per row
    return w @ V
x = np.random.default_rng(0).normal(size=(4, 8))      # 4 tokens, 8-dim embeddings
print(attention(x, x, x).shape)                       # (4, 8)
```

## Common mistakes
- Thinking bigger is always better; small fine-tuned models often win on narrow tasks.
- Ignoring the token limit and cost when building apps.

## Learn more
- [Karpathy: Let's build GPT (in Zero to Hero)](https://karpathy.ai/zero-to-hero.html) · Free · Video
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) · Free · Course

## Practice project
Fine-tune a small pretrained transformer to classify Urdu or English text.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
