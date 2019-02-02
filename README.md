# flipkart-grid
Flipkart GRiD – Te[a]ch The Machines | 2019

## Level 2

- Vertical Classification using images.
- Develop a model that localizes (bounding box) the object in an image.
    + Given an image model should produce coordinates of the rectangle where in the object lies.

### DataSet

- Metadeta file: 
    + `name-of-image` -> `(x1, x2, y1, y2)`
        + `(x1, y1)` -> Bottom Left
        + `(x2, y2` -> Top Right 

### Performance metric

- Mean intersection over union of the areas.

### Ideas

#### YOLO v3
- YOLOv3 seems to be the SOTA in object detection.
    + Is there something I am missing?
- [Try this First](https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606). Seems easy enough.
- [Darknet implementation](https://pjreddie.com/darknet/yolo/)
    + Seems Pretty Straight Forward.
