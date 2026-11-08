# Machine Learning Roadmap: notes and projects

My free, step-by-step path to learning machine learning: **notes for 34 topics** and **a runnable project for every stage**, from Python basics to LLMs, RAG and AI agents.

**Interactive version:** [abbasisarah.github.io/roadmap](https://abbasisarah.github.io/roadmap/). Click through the tree, open any topic, and track your progress.

Every note follows the same format: the idea in one sentence, key ideas, a short code example, common mistakes, the best free resources, and a practice project. 🔥 = trending topic.

| # | Stage | Notes | Project |
|---|---|---|---|
| 1 | **Python & Tools** (3–4 weeks) | [Python basics](notes/01-python/python-basics.md) · [NumPy](notes/01-python/numpy.md) · [Pandas](notes/01-python/pandas.md) · [Data visualisation](notes/01-python/visualisation.md) · [Git & GitHub](notes/01-python/git.md) | [01-expense-analyser](projects/01-expense-analyser) |
| 2 | **Math for ML** (4–6 weeks (alongside coding)) | [Linear algebra](notes/02-math/linear-algebra.md) · [Calculus & gradients](notes/02-math/calculus.md) · [Probability & statistics](notes/02-math/stats.md) | [02-gradient-descent](projects/02-gradient-descent) |
| 3 | **Data Skills** (3–4 weeks) | [Data cleaning](notes/03-data/cleaning.md) · [Exploratory data analysis](notes/03-data/eda.md) · [Feature engineering](notes/03-data/features.md) · [SQL](notes/03-data/sql.md) | [03-data-cleaning](projects/03-data-cleaning) |
| 4 | **Classic Machine Learning** (6–8 weeks) | [Regression & classification](notes/04-classic-ml/supervised.md) · [Trees, forests & boosting](notes/04-classic-ml/trees.md) · [Clustering & PCA](notes/04-classic-ml/unsupervised.md) · [Evaluation & avoiding leakage](notes/04-classic-ml/evaluation.md) | [04-model-comparison](projects/04-model-comparison) |
| 5 | **Deep Learning** (8–10 weeks) | [Neural networks & backpropagation](notes/05-deep-learning/neural-nets.md) · [PyTorch](notes/05-deep-learning/pytorch.md) · [CNNs for images](notes/05-deep-learning/cnn.md) · [Transformers & attention](notes/05-deep-learning/transformers.md) 🔥 | [05-neural-net-from-scratch](projects/05-neural-net-from-scratch) |
| 6 | **Choose a Specialisation** (8–12 weeks) | [Prompt engineering](notes/06-specialise/prompting.md) 🔥 · [RAG (chat with your documents)](notes/06-specialise/rag.md) 🔥 · [Fine-tuning](notes/06-specialise/fine-tuning.md) 🔥 · [AI agents](notes/06-specialise/agents.md) 🔥 · [Computer Vision](notes/06-specialise/vision.md) · [Time Series & Forecasting](notes/06-specialise/time-series.md) · [Image generation](notes/06-specialise/diffusion.md) 🔥 | [06-forecasting-and-rag](projects/06-forecasting-and-rag) |
| 7 | **Deploy & MLOps** (4–6 weeks) | [Web demos](notes/07-deploy/demos.md) · [APIs & Docker](notes/07-deploy/apis.md) · [MLOps](notes/07-deploy/mlops.md) | [07-model-api](projects/07-model-api) |
| 8 | **Portfolio & Career** (Ongoing) | [GitHub portfolio](notes/08-career/portfolio.md) · [Kaggle competitions](notes/08-career/kaggle.md) · [Responsible AI](notes/08-career/ethics.md) · [Share what you learn](notes/08-career/share.md) | [08-portfolio-readme](projects/08-portfolio-readme) |

## Projects
Each runs on a normal laptop in seconds, using only NumPy, Pandas, scikit-learn and Matplotlib (except stage 7, which adds FastAPI).

| Project | What it shows | Result |
|---|---|---|
| [01 Expense analyser](projects/01-expense-analyser) | Pandas group-by and clear charts | Spending per category and month |
| [02 Gradient descent](projects/02-gradient-descent) | Training from scratch | Matches the exact solution: 34.96 + 5.43 × hours |
| [03 Data cleaning](projects/03-data-cleaning) | Fixing messy real-world data, with a log | 320 messy rows → 300 clean rows |
| [04 Model comparison](projects/04-model-comparison) | Honest evaluation, baselines | ROC-AUC 0.995; 92.9% of cancers caught |
| [05 Neural net from scratch](projects/05-neural-net-from-scratch) | Backpropagation by hand | 94.7% test accuracy |
| [06 Forecasting + RAG](projects/06-forecasting-and-rag) | Time series; retrieval for LLMs | 25% lower error than the naive forecast |
| [07 Model API](projects/07-model-api) | FastAPI + Docker | /predict endpoint with input validation |
| [08 Portfolio README](projects/08-portfolio-readme) | Presenting your work | A template recruiters can read in a minute |

```bash
pip install -r requirements.txt
cd projects/04-model-comparison && python compare_models.py
```

## Colab exercises
Beginner exercises you can run in your browser with no installation: step-by-step code, exercises and solutions. See [colab/](colab/).

| Exercise | Open |
|---|---|
| Predict a student's exam score (Linear Regression) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbbasiSarah/ml-roadmap/blob/main/colab/01-predict-exam-score-linear-regression.ipynb) |
| Name a flower (KNN) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbbasiSarah/ml-roadmap/blob/main/colab/02-iris-flowers-knn.ipynb) |
| Will this student pass? (Decision Tree) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbbasiSarah/ml-roadmap/blob/main/colab/03-pass-or-fail-decision-tree.ipynb) |
| Find customer groups (K-Means) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbbasiSarah/ml-roadmap/blob/main/colab/04-customer-groups-kmeans.ipynb) |
| Build a spam filter (Naive Bayes) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbbasiSarah/ml-roadmap/blob/main/colab/05-spam-filter-naive-bayes.ipynb) |
| Read handwriting (CNN) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbbasiSarah/ml-roadmap/blob/main/colab/06-handwritten-digits-cnn.ipynb) |

## All resources
Every course, book and video used in the roadmap is listed in [RESOURCES.md](RESOURCES.md). Almost all are free.

## More from me
- Website: [abbasisarah.github.io](https://abbasisarah.github.io)
- Instagram: [@shecodess.ai](https://www.instagram.com/shecodess.ai/)
- Projects: [github.com/AbbasiSarah](https://github.com/AbbasiSarah)

*Sara Abbasi · SheCodesAI · Don't just dream, Code !t*
