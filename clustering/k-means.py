from sklearn.cluster import KMeans
from tqdm import tqdm
from utils import load_data
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    images = "data/images.txt"
    names = "data/names.txt"
    X, names = load_data(images, names)
    optimal_k(X, maxk=50)
