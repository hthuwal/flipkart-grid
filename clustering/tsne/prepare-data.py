"""Conform data for tsne script

Read every image in tarin_dir and creates two files

1. image.txt
    - Each line corresponds to a flattened version of each image (resized to 24x24)
2. names.txt
    - Each line corresponds to the name of the file

"""

import os
from PIL import Image
from tqdm import tqdm
import numpy as np
import sys

train_dir = sys.argv[1]


with open("images.txt", "w") as imgs, open("names.txt", "w") as names:
    files = os.listdir(train_dir)
    for file in tqdm(files, total=len(files), ascii=True):
        _, ext = os.path.splitext(file)
        if ext == ".txt":
            continue
        file = os.path.join(train_dir, file)

        # Resize the image to 24x24
        im = Image.open(file).resize((24, 24))
        im = np.array(im)
        im = im.flatten().astype(str)

        # Write Image and corresponding file name to a file
        imgs.write(" ".join(im) + "\n")
        names.write(file + "\n")
