from sklearn.cluster import DBSCAN
from collections import Counter
from utils import load_data

if __name__ == '__main__':
    images = "data/images.txt"
    names = "data/names.txt"
    X, names = load_data(images, names)
    dbscan = DBSCAN()
    dbscan.fit(X)
    print(Counter(dbscan.labels_))
