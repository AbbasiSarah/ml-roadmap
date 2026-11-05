# Clustering & PCA

*Classic Machine Learning* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#unsupervised)

> **In one sentence:** Unsupervised learning finds structure without labels: groups (clustering) and simpler views of the data (PCA).

## Key ideas
- K-means groups points around k centres; choose k with the elbow or silhouette score.
- DBSCAN finds clusters of any shape and marks outliers.
- PCA compresses many correlated columns into a few components, useful for plotting and speed.
- Always scale features before distance-based methods.

## Example
```python
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

X = StandardScaler().fit_transform(load_iris().data)
labels = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(X)
X2 = PCA(n_components=2).fit_transform(X)     # plot X2 coloured by labels
```

## Common mistakes
- Forgetting to scale, so one big column dominates distances.
- Treating clusters as truth; they are a lens, so check they make sense.

## Learn more
- [scikit-learn: clustering guide](https://scikit-learn.org/stable/modules/clustering.html) · Free · Docs

## Practice project
Segment customers of a shopping dataset into groups and describe each group.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
