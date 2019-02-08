import numpy as np
import pickle
import pylab

from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA

if __name__ == "__main__":
    images = "images.txt"
    names = "names.txt"

    print("Loading Images...")
    X = np.loadtxt(images)
    print("Normalizing them...")
    X = normalize(X, axis=0)
    print("Loading Names...")
    names = np.loadtxt(names, dtype=str)

    # Apply PCA to reduce dimensions
    X = PCA(n_components=50).fit_transform(X)

    # Apply Using approximate O(NlogN) method
    # To use exact method O(N^2)
    Y = TSNE(n_components=2, verbose=2, n_iter=10000).fit_transform(X)

    pickle.dump([Y, names], open("2d-data.pickle", "wb"))
    pylab.clf()
    pylab.scatter(Y[:, 0], Y[:, 1], 20, names)
    pylab.savefig('plot.png')
