import csv
import os
from tqdm import tqdm
from PIL import Image

source_dir = "hc/images"
train_dir = "hc/train"

boxes = open("hc/training.csv")

print("Reading Labels...")
with open("../clustering/results/labelled-data.txt") as f:
    labels = f.readlines()
    for i in tqdm(range(len(labels)), ascii=True):
        labels[i] = labels[i].split(",")
        labels[i] = (labels[i][0], int(labels[i][-1]))
    labels = dict(labels)

with open("hc/training.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in tqdm(reader, total=14000, ascii=True):
        image = row[0]
        x1, x2, y1, y2 = list(map(int, row[1:]))
        tf = os.path.join(train_dir, image)
        af = os.path.join(train_dir, os.path.splitext(image)[0] + ".txt")

        im = Image.open(tf)
        iw, ih = im.size

        x = (x1 + x2) / (2 * iw)
        y = (y1 + y2) / (2 * ih)
        width = (x2 - x1) / iw
        height = (y2 - y1) / ih

        with open(af, "w") as annot:
            annot.write("{} {} {} {} {}".format(labels[image], x, y, width, height))
