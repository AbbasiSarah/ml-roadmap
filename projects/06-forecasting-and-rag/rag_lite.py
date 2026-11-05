"""Stage 6 project (LLM track): the retrieval half of RAG, searching your own ML notes.

    python rag_lite.py "what is data leakage?"

It splits every note in ../../notes into chunks, finds the chunks most relevant to your question
and builds the prompt you would send to an LLM. Plug in any LLM API to complete the "G" in RAG.
"""
import re
import sys
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

NOTES = Path(__file__).resolve().parents[2] / "notes"


def load_chunks():
    chunks = []
    for f in sorted(NOTES.rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ")
        for part in re.split(r"\n## ", text)[1:]:                       # skip the title block
            heading = part.splitlines()[0]
            if heading in ("Learn more", "Example"):                       # links and code are poor search text
                continue
            body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", part)          # keep link text, drop URLs
            body = body.split("\n---")[0].strip()
            chunks.append((f"{title} › {heading}", f"{title}. {body}"))
    return chunks


def retrieve(question, k=3):
    chunks = load_chunks()
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2)).fit([c[1] for c in chunks])
    sims = cosine_similarity(vec.transform([question]), vec.transform([c[1] for c in chunks]))[0]
    top = sims.argsort()[::-1][:k]
    return [(chunks[i][0], chunks[i][1], sims[i]) for i in top]


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "What is data leakage and how do I avoid it?"
    hits = retrieve(q)
    print(f"Question: {q}\n")
    for src, text, s in hits:
        print(f"[{s:.2f}] {src}\n    {text[:220].replace(chr(10), ' ')}...\n")
    context = "\n\n".join(f"Source: {src}\n{text}" for src, text, _ in hits)
    prompt = f"Answer using only the sources below. Cite the source. If the answer isn't there, say so.\n\n{context}\n\nQuestion: {q}"
    print(f"--- prompt for the LLM ({len(prompt)} characters) built; send it to any LLM API ---")
