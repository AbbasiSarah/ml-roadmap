NOTES = {}

NOTES["supervised"] = dict(
    one="Supervised learning learns from examples with known answers to predict a number (regression) or a category (classification).",
    ideas=["Split data: train to learn, validation to choose, test to report, used once.",
           "Start with a baseline (predict the average or the most common class) so you know what \"good\" means.",
           "Linear and logistic regression are fast, explainable starting points.",
           "Regression metrics: MAE, RMSE, R². Classification: accuracy, precision, recall, F1, ROC-AUC."],
    code='''from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)
print("test accuracy:", model.score(Xte, yte))''',
    mistakes=["Reporting training accuracy as the result.",
              "Using accuracy on imbalanced data (99% \"not spam\" is useless)."])

NOTES["trees"] = dict(
    one="Decision trees split data with yes/no questions; forests and boosting combine many trees and win on most table data.",
    ideas=["A single tree is easy to explain but overfits.",
           "Random forest = many trees on random samples, averaged: robust with little tuning.",
           "Gradient boosting (XGBoost, LightGBM, scikit-learn HistGradientBoosting) adds trees that fix previous errors, and is usually the most accurate.",
           "Trees need no scaling and handle non-linear patterns automatically.",
           "Feature importance (prefer permutation importance) shows what drives predictions."],
    code='''from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
for m in [RandomForestClassifier(300, random_state=0), HistGradientBoostingClassifier(random_state=0)]:
    print(type(m).__name__, cross_val_score(m, X, y, cv=5).mean().round(3))''',
    mistakes=["Very deep single trees that memorise the training set.",
              "Trusting default impurity importance, which is biased towards many-valued features."])

NOTES["unsupervised"] = dict(
    one="Unsupervised learning finds structure without labels: groups (clustering) and simpler views of the data (PCA).",
    ideas=["K-means groups points around k centres; choose k with the elbow or silhouette score.",
           "DBSCAN finds clusters of any shape and marks outliers.",
           "PCA compresses many correlated columns into a few components, useful for plotting and speed.",
           "Always scale features before distance-based methods."],
    code='''from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

X = StandardScaler().fit_transform(load_iris().data)
labels = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(X)
X2 = PCA(n_components=2).fit_transform(X)     # plot X2 coloured by labels''',
    mistakes=["Forgetting to scale, so one big column dominates distances.",
              "Treating clusters as truth; they are a lens, so check they make sense."])

NOTES["evaluation"] = dict(
    one="Honest evaluation means testing on data the model truly never saw. It separates real results from fake 99% accuracy.",
    ideas=["Cross-validation averages several train/test splits for a stable estimate.",
           "Group splits: if one person or place has many rows, keep all of them on the same side (`GroupKFold`).",
           "Time series: always train on the past and test on the future.",
           "Leakage = information from the test set or the future reaching training (duplicates, scaling on all data, target-derived features).",
           "Pick metrics for the cost of mistakes: missed cancer ≠ false alarm."],
    code='''from sklearn.model_selection import GroupKFold, cross_val_score
# rows from the same patient must not be in both train and test
scores = cross_val_score(model, X, y, groups=patient_id, cv=GroupKFold(5), scoring="roc_auc")
print(scores.mean(), scores.std())''',
    mistakes=["Random splits on data with repeated people, days or places.",
              "Tuning on the test set; it is then no longer a test.",
              "Not removing duplicate rows before splitting."])

NOTES["neural-nets"] = dict(
    one="A neural network is layers of weighted sums plus non-linear activations, trained by sending the error backwards (backpropagation).",
    ideas=["Neuron: output = activation(w · x + b). ReLU is the default activation.",
           "Loss measures error: MSE for numbers, cross-entropy for classes.",
           "Backpropagation = chain rule; it gives the gradient for every weight.",
           "Optimisers (SGD, Adam) update weights with those gradients.",
           "Overfitting fixes: more data, dropout, weight decay, early stopping."],
    code='''import numpy as np
X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])     # XOR inputs + a constant 1 (bias)
y = np.array([[0],[1],[1],[0]])
rng = np.random.default_rng(0); W1, W2 = rng.normal(size=(3, 8)), rng.normal(size=(8, 1))
sig = lambda z: 1 / (1 + np.exp(-z))
for _ in range(5000):
    h = np.tanh(X @ W1); p = sig(h @ W2)
    d2 = p - y                          # gradient of cross-entropy wrt logits
    W2 -= 0.1 * h.T @ d2
    W1 -= 0.1 * X.T @ ((d2 @ W2.T) * (1 - h**2))
print(p.round(2).ravel())               # ~[0, 1, 1, 0]''',
    mistakes=["Not normalising inputs.",
              "Judging training only by training loss; watch validation loss."])

NOTES["pytorch"] = dict(
    one="PyTorch builds and trains neural networks with automatic gradients and GPU support. It is the standard in research and industry.",
    ideas=["Tensors are NumPy arrays that can live on a GPU and track gradients.",
           "`nn.Module` defines a model; `forward` describes the computation.",
           "Training loop: forward → loss → `loss.backward()` → `optimizer.step()` → `optimizer.zero_grad()`.",
           "`model.train()` vs `model.eval()` changes dropout and batch norm behaviour.",
           "`DataLoader` handles batching and shuffling."],
    code='''import torch, torch.nn as nn
model = nn.Sequential(nn.Linear(10, 32), nn.ReLU(), nn.Linear(32, 2))
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()
for xb, yb in loader:                   # loader = DataLoader(dataset, batch_size=64, shuffle=True)
    loss = loss_fn(model(xb), yb)
    opt.zero_grad(); loss.backward(); opt.step()''',
    mistakes=["Forgetting `zero_grad()`, so gradients pile up.",
              "Evaluating without `torch.no_grad()` and `model.eval()`."])

NOTES["cnn"] = dict(
    one="Convolutional networks slide small filters over images to detect edges, then shapes, then objects.",
    ideas=["A convolution filter (e.g. 3×3) shares its weights across the whole image, so it needs far fewer parameters than a dense layer.",
           "Pooling shrinks the image and adds tolerance to small shifts.",
           "Deeper layers see larger areas and more abstract features.",
           "Transfer learning: start from a network pretrained on millions of images and fine-tune it on yours."],
    code='''import torch.nn as nn
cnn = nn.Sequential(
    nn.Conv2d(1, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),    # 28 -> 14
    nn.Conv2d(8, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),   # 14 -> 7
    nn.Flatten(), nn.Linear(16 * 7 * 7, 64), nn.ReLU(), nn.Linear(64, 10))''',
    mistakes=["Training from scratch on a few hundred images; use transfer learning.",
              "No data augmentation (flips, shifts, crops)."])

NOTES["transformers"] = dict(
    one="Transformers use attention to let every word look at every other word. This architecture powers ChatGPT and most modern AI.",
    ideas=["Text is split into tokens and turned into vectors (embeddings).",
           "Self-attention: each token scores how relevant every other token is (a dot product), then mixes their information.",
           "Positional encodings tell the model the word order.",
           "Pretrain on huge text by predicting the next token; then fine-tune or prompt for tasks.",
           "Encoder models (BERT) suit classification; decoder models (GPT) generate text."],
    code='''import numpy as np
def attention(Q, K, V):
    scores = Q @ K.T / np.sqrt(K.shape[1])            # how much each token attends to each other
    w = np.exp(scores - scores.max(1, keepdims=True))
    w /= w.sum(1, keepdims=True)                      # softmax per row
    return w @ V
x = np.random.default_rng(0).normal(size=(4, 8))      # 4 tokens, 8-dim embeddings
print(attention(x, x, x).shape)                       # (4, 8)''',
    mistakes=["Thinking bigger is always better; small fine-tuned models often win on narrow tasks.",
              "Ignoring the token limit and cost when building apps."])

NOTES["prompting"] = dict(
    one="Prompt engineering means giving an LLM clear instructions, context and examples so it does the task reliably.",
    ideas=["Be specific: role, task, audience, format and length.",
           "Give examples of good output (few-shot).",
           "Ask for structured output (JSON, a table) when code will read it.",
           "Break big tasks into steps; ask the model to check its own answer.",
           "Test prompts on many inputs, not one lucky example."],
    code='''prompt = """You are a meeting assistant.
Turn the notes below into a task list.
Format: one line per task as "- [owner] task (due date or 'no date')".
Only include tasks actually agreed in the meeting.

Notes:
{notes}"""''',
    mistakes=["Vague prompts (\"make it better\").",
              "Trusting outputs without checking facts; LLMs can invent things."])

NOTES["rag"] = dict(
    one="RAG (retrieval-augmented generation) lets an LLM answer from your own documents: it first searches them, then answers using what it found.",
    ideas=["Split documents into chunks; turn each chunk into an embedding vector.",
           "Store vectors in a vector database (FAISS, Chroma, pgvector).",
           "At question time: embed the question, retrieve the most similar chunks, and put them in the prompt.",
           "Ask the model to cite which chunk each answer came from, and to say \"I don't know\" if it isn't there.",
           "Evaluate retrieval (did we find the right chunk?) separately from generation."],
    code='''# retrieval step with TF-IDF (no GPU needed); swap in embeddings later
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
chunks = ["Fees are due by the 10th of each month.", "Exams start on 1 June.", "The library opens at 8am."]
vec = TfidfVectorizer().fit(chunks)
q = "When do exams begin?"
best = cosine_similarity(vec.transform([q]), vec.transform(chunks)).argmax()
print(chunks[best])     # -> put this chunk into the LLM prompt as context''',
    mistakes=["Chunks too big or too small; around 200–500 words is a good start.",
              "Not telling the model to stay within the retrieved context."])

NOTES["fine-tuning"] = dict(
    one="Fine-tuning continues training a pretrained model on your examples so it learns your task or style.",
    ideas=["Try prompting and RAG first; fine-tune when you need a consistent style, format or a smaller, cheaper model.",
           "Quality beats quantity: a few hundred clean examples can be enough.",
           "LoRA/QLoRA train small adapter weights, so it fits on a single GPU.",
           "Hold out test examples and compare against the base model."],
    code='''from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
name = "distilbert-base-uncased"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name, num_labels=2)
ds = load_dataset("imdb").map(lambda b: tok(b["text"], truncation=True), batched=True)
Trainer(model=model, args=TrainingArguments("out", num_train_epochs=1),
        train_dataset=ds["train"].shuffle(seed=0).select(range(2000)),
        eval_dataset=ds["test"].select(range(500)), tokenizer=tok).train()''',
    mistakes=["Fine-tuning to add facts (use RAG for knowledge).",
              "No evaluation set, so you can't tell if it improved."])

NOTES["agents"] = dict(
    one="An AI agent is an LLM in a loop that plans, calls tools (search, code, APIs) and acts until a task is done.",
    ideas=["Loop: think → choose a tool → read the result → repeat → final answer.",
           "Tools are functions with clear names, descriptions and input schemas.",
           "Guardrails: limit steps, check tool inputs, and require human approval for risky actions.",
           "Log every step so you can debug what the agent did.",
           "Start with one or two tools; most failures come from vague tool descriptions."],
    code='''TOOLS = {"calculator": lambda expr: str(eval(expr, {"__builtins__": {}})),   # demo only
         "search_notes": lambda q: "Exams start on 1 June."}

def run_agent(llm, task, max_steps=5):
    history = [f"Task: {task}"]
    for _ in range(max_steps):
        action = llm("\\n".join(history) + "\\nReply TOOL:<name>:<input> or FINAL:<answer>")
        if action.startswith("FINAL:"):
            return action[6:]
        _, name, arg = action.split(":", 2)
        history.append(f"{name}({arg}) -> {TOOLS[name](arg)}")''',
    mistakes=["Giving agents powerful tools (payments, deleting files) without approval steps.",
              "No step limit, so it loops forever and costs money."])

NOTES["vision"] = dict(
    one="Computer vision teaches machines to understand images: classify, detect objects, segment pixels.",
    ideas=["Classification: what is in the image. Detection: where (boxes). Segmentation: which pixels.",
           "Pretrained backbones (ResNet, ViT) plus fine-tuning work with small datasets.",
           "Augmentation (flip, crop, colour) is essential.",
           "Medical and satellite images need careful, expert-checked labels."],
    code='''from transformers import pipeline
detector = pipeline("object-detection", model="facebook/detr-resnet-50")
for obj in detector("street.jpg"):
    if obj["score"] > 0.8:
        print(obj["label"], round(obj["score"], 2), obj["box"])''',
    mistakes=["Train and test images from the same video or patient (leakage).",
              "Ignoring class imbalance (few examples of the rare object)."])

NOTES["time-series"] = dict(
    one="Time-series forecasting predicts the future from the past: sales, demand, weather, health signals.",
    ideas=["Look for trend, seasonality (weekly, yearly) and holidays.",
           "Always beat a naive baseline: \"tomorrow = today\" or \"same week last year\".",
           "Split by time: train on the past, test on the future (rolling-origin evaluation).",
           "Lag features (yesterday, last week) let ordinary ML models forecast.",
           "Report error in units people understand (e.g. ±120 units, MAPE)."],
    code='''import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
s = pd.read_csv("sales.csv", parse_dates=["date"], index_col="date")["sales"]
df = pd.DataFrame({"y": s, "lag1": s.shift(1), "lag7": s.shift(7), "dow": s.index.dayofweek}).dropna()
train, test = df[:-30], df[-30:]                       # last 30 days = future
m = HistGradientBoostingRegressor().fit(train.drop(columns="y"), train.y)
print("MAE:", (m.predict(test.drop(columns="y")) - test.y).abs().mean())''',
    mistakes=["Random shuffling of time-series data.",
              "Not comparing with a naive baseline."])

NOTES["diffusion"] = dict(
    one="Diffusion models generate images by starting from noise and removing it step by step, guided by a text prompt.",
    ideas=["Training: add noise to images, teach a network to predict that noise.",
           "Generation: start from pure noise and denoise in many small steps.",
           "Text guidance comes from a text encoder; guidance scale trades creativity for prompt-following.",
           "Ethics: consent, copyright and deepfakes matter. Label AI-generated images."],
    code='''from diffusers import StableDiffusionPipeline
import torch
pipe = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",
                                               torch_dtype=torch.float16).to("cuda")
image = pipe("a watercolour of a robot reading a book in Lahore", num_inference_steps=30).images[0]
image.save("robot.png")''',
    mistakes=["Generating real people's likeness without consent.",
              "Expecting exact text or hands; check outputs carefully."])

NOTES["demos"] = dict(
    one="A web demo turns your model into something anyone can try, which is the fastest way to impress.",
    ideas=["Gradio and Streamlit build a UI in a few lines of Python.",
           "Hugging Face Spaces and Streamlit Community Cloud host demos for free.",
           "Small models can even run in the browser in JavaScript (like my digit demo).",
           "Add example inputs and a clear note on what the model can't do."],
    code='''import gradio as gr, pickle
model = pickle.load(open("spam_model.pkl", "rb"))
def classify(msg):
    p = model.predict_proba([msg])[0, 1]
    return {"spam": p, "not spam": 1 - p}
gr.Interface(classify, gr.Textbox(label="SMS message"), gr.Label()).launch()''',
    mistakes=["Demos that crash on unusual input; validate inputs.",
              "No explanation of limitations."])

NOTES["apis"] = dict(
    one="An API lets other apps send data to your model and get predictions back; Docker packages it to run anywhere.",
    ideas=["FastAPI: define a function, get an HTTP endpoint with automatic docs.",
           "Validate input with Pydantic models.",
           "Load the model once at start-up, not on every request.",
           "Dockerfile = recipe for the environment, so \"works on my machine\" works everywhere."],
    code='''from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()
model = pickle.load(open("spam_model.pkl", "rb"))

class Msg(BaseModel):
    text: str

@app.post("/predict")
def predict(m: Msg):
    return {"spam_probability": float(model.predict_proba([m.text])[0, 1])}
# run: uvicorn app:app --reload   then open http://127.0.0.1:8000/docs''',
    mistakes=["Exposing an API publicly without authentication or rate limits.",
              "Different library versions in training vs serving; pin them."])

NOTES["mlops"] = dict(
    one="MLOps keeps models reliable after launch: tracking experiments, versioning data, retraining and monitoring.",
    ideas=["Track every experiment: data version, parameters, metrics (MLflow, Weights & Biases).",
           "Automate: tests and retraining pipelines (GitHub Actions, Airflow).",
           "Monitor data drift: when real inputs change, accuracy silently drops.",
           "Keep a model card: what it's for, data, metrics, limitations."],
    code='''import mlflow
with mlflow.start_run():
    mlflow.log_param("model", "random_forest"); mlflow.log_param("n_estimators", 300)
    mlflow.log_metric("val_auc", 0.91)
    mlflow.sklearn.log_model(model, "model")''',
    mistakes=["\"Final_model_v7_really_final.pkl\" with no record of how it was made.",
              "Never checking a deployed model's accuracy again."])

NOTES["portfolio"] = dict(
    one="A portfolio is 3–5 projects that show you can solve real problems end to end and explain them clearly.",
    ideas=["Each README: problem → data → method → result in numbers → chart → how to run → limitations.",
           "Show judgement: baselines, honest evaluation, what didn't work.",
           "A live demo link gets clicked far more than code.",
           "Pin your best repositories; add topics and descriptions."],
    code='''## Results
| Model | Precision | Recall | F1 |
|---|---|---|---|
| Baseline (always "ham") | 0% | 0% | 0.00 |
| **Linear SVM** | **99.2%** | **94.7%** | **0.969** |

Try it: `python predict.py "WINNER!! Claim your prize"`''',
    mistakes=["Copying tutorial projects (Titanic, Iris) with no twist.",
              "No README or results; recruiters won't run your code."])

NOTES["kaggle"] = dict(
    one="Kaggle gives you real datasets, competitions and thousands of public solutions to learn from.",
    ideas=["Start with \"Getting Started\" competitions (Titanic, House Prices, Digit Recognizer).",
           "Read top public notebooks after you try yourself.",
           "Publish clean notebooks; good ones earn medals and visibility.",
           "Trust your cross-validation more than the public leaderboard."],
    code='''# Typical submission
import pandas as pd
test = pd.read_csv("test.csv")
pd.DataFrame({"Id": test.Id, "SalePrice": model.predict(test[features])}).to_csv("submission.csv", index=False)''',
    mistakes=["Overfitting the public leaderboard.",
              "Copying notebooks without understanding them."])

NOTES["ethics"] = dict(
    one="Responsible AI asks who could be harmed by a model and makes sure results are fair, private and honestly reported.",
    ideas=["Bias: check performance separately for groups (gender, age, region).",
           "Privacy: anonymise data and collect only what you need.",
           "Transparency: explain what the model does and where it fails.",
           "Honesty: report realistic evaluation, including negative results."],
    code='''import pandas as pd
from sklearn.metrics import recall_score
res = pd.DataFrame({"group": groups, "y": y_true, "pred": y_pred})
print(res.groupby("group").apply(lambda g: recall_score(g.y, g.pred)))   # big gaps = investigate''',
    mistakes=["Only reporting overall accuracy.",
              "Using personal data without consent."])

NOTES["share"] = dict(
    one="Sharing what you learn, through posts, reels and talks, builds your name, and teaching is the fastest way to understand something yourself.",
    ideas=["Explain one idea at a time, with one picture.",
           "Show your process, including mistakes; people relate to it.",
           "Link every post to a project or the code.",
           "Consistency beats perfection: one post a week compounds."],
    code='''Post template
1. Hook: "I trained a neural network without TensorFlow. Here's what I learned."
2. One idea, explained simply, with a visual.
3. Result in a number.
4. Link: GitHub / live demo.
5. Question to the audience.''',
    mistakes=["Waiting until you're an \"expert\" to start.",
              "Posts with no link to your work."])
