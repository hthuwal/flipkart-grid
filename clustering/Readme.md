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

