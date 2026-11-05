# Web demos

*Deploy & MLOps* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#demos)

> **In one sentence:** A web demo turns your model into something anyone can try, which is the fastest way to impress.

## Key ideas
- Gradio and Streamlit build a UI in a few lines of Python.
- Hugging Face Spaces and Streamlit Community Cloud host demos for free.
- Small models can even run in the browser in JavaScript (like my digit demo).
- Add example inputs and a clear note on what the model can't do.

## Example
```python
import gradio as gr, pickle
model = pickle.load(open("spam_model.pkl", "rb"))
def classify(msg):
    p = model.predict_proba([msg])[0, 1]
    return {"spam": p, "not spam": 1 - p}
gr.Interface(classify, gr.Textbox(label="SMS message"), gr.Label()).launch()
```

## Common mistakes
- Demos that crash on unusual input; validate inputs.
- No explanation of limitations.

## Learn more
- [Hugging Face Spaces docs](https://huggingface.co/docs/hub/spaces) · Free · Docs
- [Streamlit docs](https://docs.streamlit.io/) · Free · Docs

## Practice project
Publish one of your models as a free web app and share the link.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
