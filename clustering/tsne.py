import os
import pickle
import pylab

from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from utils import load_data

if __name__ == "__main__":
    images = "data/images.txt"
    names = "data/names.txt"

    X, names = load_data(images, names)
    print("Normalizing them...")
    X = normalize(X, axis=0)
    # Apply PCA to reduce dimensions
    X = PCA(n_components=50).fit_transform(X)
    tsne = TSNE(
        n_components=2,
        verbose=2,
        n_iter=1000,
        perplexity=50,
        early_exaggeration=20
    )
    Y = tsne.fit_transform(X)

    if not os.path.exists("results"):
        os.makedirs("results")

    pickle.dump([Y, names], open("results/2d-tsne-data.pickle", "wb"))
    pylab.clf()
    pylab.scatter(Y[:, 0], Y[:, 1], s=1)
    pylab.savefig('results/2d-tsne-plot.png')
