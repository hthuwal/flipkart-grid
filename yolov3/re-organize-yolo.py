"""Conform Data to yolov3 Format

Assumption:
    - All Images Present in source_dir
    - A training.csv file with each row depicting the following
        - Image_Name,x1,x2,y1,y2
            - Here x1, y1 and x2, y2 are bottom left and top right coordinates
            of the bounding box in the image

Moves the trainig images as per training.csv from source_dir to
train_dir and creates a txt file corresponding to each image with containing
`class x y w h`

Note that (x,y) and (w,h) are coordinates and dimensions of the bounding
box relative to width and height of the entire image.

"""


import csv
import os
import shutil
from tqdm import tqdm
from PIL import Image

source_dir = "hc/images"
train_dir = "hc/train"
test_dir = "hc/test"

print("Moving Train Data...")
if not os.path.exists(train_dir):
    os.makedirs(train_dir)

with open("hc/training.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in tqdm(reader, ascii=True, total=14000):
        image = row[0]
        x1, x2, y1, y2 = list(map(int, row[1:]))
        sf = os.path.join(source_dir, image)
        tf = os.path.join(train_dir, image)
        af = os.path.join(train_dir, os.path.splitext(image)[0] + ".txt")

        im = Image.open(sf)
        iw, ih = im.size

        x = (x1 + x2) / (2 * iw)
        y = (y1 + y2) / (2 * ih)
        width = (x2 - x1) / iw
        height = (y2 - y1) / ih

        shutil.move(sf, tf)
        with open(af, "w") as annot:
            annot.write("0 {} {} {} {}".format(x, y, width, height))

print("Moving Test Data...")
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

with open("hc/test.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in tqdm(reader, ascii=True, total=12815):
        image = row[0]
        sf = os.path.join(source_dir, image)
        tf = os.path.join(test_dir, image)
        shutil.move(sf, tf)
