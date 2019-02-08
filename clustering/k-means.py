from sklearn.cluster import KMeans
from tqdm import tqdm
from utils import load_data, load_pickled_data
from collections import Counter
import matplotlib.pyplot as plt
import os


def optimal_k(X, maxk=50):
    errs = []
    Ks = range(1, maxk + 1)
    for k in tqdm(Ks, ascii=True):
        km = KMeans(n_clusters=k)
        km = km.fit(X)
        errs.append(km.inertia_)

    print(errs)
    plt.plot(Ks, errs, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.savefig("results/kmeans.png")


def dump_labels(k):
    kmean = KMeans(n_clusters=k)
    kmean.fit(X)
    labels = kmean.labels_
    values = list(Counter(labels).items())
    values.sort(key=lambda x: x[0])
    x, y = zip(*values)
    plt.bar(x, y)
    plt.xlabel("Cluster Number")
    plt.ylabel("Number of Images")
    plt.title("Size of clusters")
    plt.savefig("results/cluster-distribution.png")
    with open("results/labelled-data.txt", "w") as out:
        for i in tqdm(range(len(names)), ascii=True):
            out.write(os.path.basename(names[i]) + "," + str(labels[i]) + "\n")


if __name__ == '__main__':
    images = "data/images.txt"
    names = "data/names.txt"
    # X, names = load_data(images, names)
    X, names = load_pickled_data("results/2d-tsne-data.pickle")
    # optimal_k(X, maxk=50)
    dump_labels(30)
