"""Stage 7 project: serve a model as a web API with FastAPI.

    pip install fastapi uvicorn scikit-learn
    python train.py
    uvicorn app:app --reload        # then open http://127.0.0.1:8000/docs and try /predict
"""
import pickle
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Spam detector API", version="1.0")
model = pickle.load(open(Path(__file__).parent / "spam_model.pkl", "rb"))   # load once at start-up


class Message(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000, examples=["WINNER! Claim your free prize now"])


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(msg: Message):
    p = float(model.predict_proba([msg.text])[0, 1])
    return {"spam_probability": round(p, 3), "label": "spam" if p >= 0.5 else "not spam"}
