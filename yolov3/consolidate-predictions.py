import csv
import os
from tqdm import tqdm

pred_dir = "hc/predictions"

with open("hc/test.csv") as f, open("hc/prediction_csvs/predictions.csv", "w") as out:
    reader = csv.reader(f)
    next(reader)
    for row in tqdm(reader, ascii=True, total=12815):
        image = row[0]
        pred_file = os.path.join(pred_dir, image + ".txt")
        if os.path.exists(pred_file):
            with open(pred_file) as pred:
                values = pred.read().strip().split()
        else:
            values = ["0"] * 4

        values.insert(0, image)
        # print(values)
        out.write(",".join(values) + "\n")
