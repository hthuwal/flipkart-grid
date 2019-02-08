import numpy as np
import pickle


def load_data(images, names):

    print("Loading Images...")
    X = np.loadtxt(images)

    print("Converting to grayscale")
    X = X.reshape(X.shape[0], 24, 24, 3)
    X = np.average(X, axis=3).reshape(X.shape[0], -1)

    print("Loading Names...")
    names = np.loadtxt(names, dtype=str)

    return X, names


def load_pickled_data(path):
    with open(path, "rb") as f:
        return pickle.load(f)
