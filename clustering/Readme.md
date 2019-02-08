## TSNE

t-Distributed Stochastic Neighbor Embedding (t-SNE) is a (prize-winning) technique for dimensionality reduction

- tsne/tsne.py   
    - ~[Old Source](https://lvdmaaten.github.io/tsne/)~
    - Now using sklearn's inbuilt function

- tsne/prepare-data.py
    - Conform data for tsne script
    - Read every image in train_dir and creates two files
        1. image.txt
            - Each line corresponds to a flattened version of each image (resized to 24x24)
        2. names.txt
            - Each line corresponds to the name of the file

- No benefit. 2D projection shows no clustering at all
    ![](results/2d-tsne-plot.png)
 
### DBSCAN 

- On 24x24 Grayscale Image
    + **Failed!!**
    + 3 clusters.
    + 13984 / 14000 points are outliers. :joy:
    ```python
    {   
        -1: 13984, 
        0: 6, 
        1: 5, 
        2: 5
    }
    ```
