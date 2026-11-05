"""Train and save the spam model that the API serves."""
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

messages = [("WINNER! Claim your free prize now, call 09061701461", 1), ("Free entry to win a cash prize, text WIN to 80086", 1),
            ("URGENT! Your account will be closed, verify at www.bank-verify.co", 1), ("You have won £1000 cash, reply YES", 1),
            ("Congratulations, you have been selected for a free iPhone, click the link", 1),
            ("Are we still meeting at 6 for dinner?", 0), ("Can you send me the notes from class?", 0),
            ("I'll be home late tonight, start without me", 0), ("Happy birthday! Hope you have a great day", 0),
            ("The meeting moved to Thursday at 10", 0)]
texts, labels = zip(*messages)
model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), LogisticRegression(C=10)).fit(texts, labels)
pickle.dump(model, open(Path(__file__).parent / "spam_model.pkl", "wb"))
print("Saved spam_model.pkl (a tiny demo model: train on the full SMS dataset for real use)")
