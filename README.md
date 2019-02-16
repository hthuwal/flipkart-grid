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

#### Results

Shortlisted for next Round :sunglasses: :heart_eyes: :yum:

1. Yolov3: Only 1 Class
    - Default Everything: 416x416
        + 88.812 Test Score Around 65th Epoch
        + 98 mAP on Validation
        - [Training-plots](yolov3/plots/plot-1-416.pdf) 

    - Default + Custom Anchor Points
        + ~85 Percent Test Score
        + 98 mAP on Validation

    - Increased Size of the image (640x640) + custom anchors
        + Took too long
        + 95 mAP on Validation 78
    
    - Mini
        + Not Promising stuck at 85% Validation

2. Yolov3: 30 Classes (K Mean Clustering)
    - 40 Training Epochs: 74.52 Test Score
    - [Training-plots](yolov3/plots/plot-30-416.pdf) 

3. Yolov3: 10 Classes (K Mean Clustering)
    - 50 Training Epochs: 79.9338 %
    - 70 Training Epochs: 81.798 %
    - [Training-plots](yolov3/plots/plot-10-416.pdf) 

## Level 3

- Same Dataset
- Larger Number of Training and Test Images with update bboxes seems to be the oly difference.

## Yolov3

- Pretrained
    + 31 epochs: 87.1057 Test Score
