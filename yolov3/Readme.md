## Source

[Ultralytics](https://github.com/ultralytics/yolov3)

### Changes from the source

- Removed code for transfer learning.
- Used Adam Optimizer instead of SGD with momentum
    + Hence no SGD Burn In.
- Added Progress Bars during Training and Testing.
    + Results are shown only after each epoch.
- The output is now of the form
    `x1 x2 y1 y2`

### Description

- cfg/yolo...cfg
    + Configuration Files defining yolo architectures.

- cfg/hc.data
    ```
    classes=1               # Number of Classes
    train=hc/train.txt      # Path to file containg path to each training image per line 
    valid=hc/valid.txt      # Path to file containg path to each validation image per line
    names=hc/hc.names       # file containing names of each class. Line i -> Name of ith class
    backup=backup/
    eval=hc
    ```
- The folder containing the training and validation images should contain a text file corresponding to each image. For e.g
    ```
    image_1.jpg
    image_1.txt
    .
    .
    ```
- image_1.txt should contain 
    + `class x y w h`
    + For e.g
        * `0 0.48671875 0.6145833333333334 0.2390625 0.6125`
    + Note that (x,y) and (w,h) are coordinates and dimensions of the bounding box relative to width and height of the entire image.

## Training

- For the first time

```bash
python train.py --data-config cfg/hc.data --cfg cfg/yolov3.cfg --batch-size 10 --epochs 10
```

- To continue from the last model

```bash
python train.py --resume --data-config cfg/hc.data --cfg cfg/yolov3.cfg --batch-size 10 --epochs 10
```

Use `python train.py -h` to see other available options.

## Testing

```bash
time python detect.py --cfg cfg/yolov3.cfg --data-config cfg/hc.data --weights weights/best.pt --image-folder hc/test --output-folder hc/predictions --txt-out True
```