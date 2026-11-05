# APIs & Docker

*Deploy & MLOps* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#apis)

> **In one sentence:** An API lets other apps send data to your model and get predictions back; Docker packages it to run anywhere.

## Key ideas
- FastAPI: define a function, get an HTTP endpoint with automatic docs.
- Validate input with Pydantic models.
- Load the model once at start-up, not on every request.
- Dockerfile = recipe for the environment, so "works on my machine" works everywhere.

## Example
```python
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()
model = pickle.load(open("spam_model.pkl", "rb"))

class Msg(BaseModel):
    text: str

@app.post("/predict")
def predict(m: Msg):
    return {"spam_probability": float(model.predict_proba([m.text])[0, 1])}
# run: uvicorn app:app --reload   then open http://127.0.0.1:8000/docs
```

## Common mistakes
- Exposing an API publicly without authentication or rate limits.
- Different library versions in training vs serving; pin them.

## Learn more
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) · Free · Docs
- [Docker: get started](https://docs.docker.com/get-started/) · Free · Docs

## Practice project
A FastAPI endpoint that returns a spam score for any message, inside a Docker container.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
