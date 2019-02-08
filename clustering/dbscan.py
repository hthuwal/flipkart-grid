from sklearn.cluster import DBSCAN
from collections import Counter
from utils import load_data, load_pickled_data

if __name__ == '__main__':
    images = "data/images.txt"
    names = "data/names.txt"

    # X, names = load_data(images, names)
    X, names = load_pickled_data("results/2d-tsne-data.pickle")
    dbscan = DBSCAN(eps=1)
    dbscan.fit(X)

    print(Counter(dbscan.labels_), len(Counter(dbscan.labels_)))
