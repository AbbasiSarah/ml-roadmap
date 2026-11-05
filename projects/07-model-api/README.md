# Serve a model as an API

*Stage 7 · Deploy & MLOps* · [All projects](../../README.md#projects)

A FastAPI web service with input validation, a health check and a /predict endpoint, plus a Dockerfile so it runs anywhere.

## Run it
```bash
pip install -r requirements.txt
python train.py
uvicorn app:app --reload   # open http://127.0.0.1:8000/docs
```

## What you practise
APIs, validation, loading a model once, Docker.
