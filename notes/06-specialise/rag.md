# RAG (chat with your documents)

*Choose a Specialisation › LLMs & Generative AI* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#rag)

> **In one sentence:** RAG (retrieval-augmented generation) lets an LLM answer from your own documents: it first searches them, then answers using what it found.

## Key ideas
- Split documents into chunks; turn each chunk into an embedding vector.
- Store vectors in a vector database (FAISS, Chroma, pgvector).
- At question time: embed the question, retrieve the most similar chunks, and put them in the prompt.
- Ask the model to cite which chunk each answer came from, and to say "I don't know" if it isn't there.
- Evaluate retrieval (did we find the right chunk?) separately from generation.

## Example
```python
# retrieval step with TF-IDF (no GPU needed); swap in embeddings later
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
chunks = ["Fees are due by the 10th of each month.", "Exams start on 1 June.", "The library opens at 8am."]
vec = TfidfVectorizer().fit(chunks)
q = "When do exams begin?"
best = cosine_similarity(vec.transform([q]), vec.transform(chunks)).argmax()
print(chunks[best])     # -> put this chunk into the LLM prompt as context
```

## Common mistakes
- Chunks too big or too small; around 200–500 words is a good start.
- Not telling the model to stay within the retrieved context.

## Learn more
- [DeepLearning.AI short courses (RAG)](https://www.deeplearning.ai/short-courses/) · Free · Course
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) · Free · Course

## Practice project
A chatbot that answers questions from your university's course handbook.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
