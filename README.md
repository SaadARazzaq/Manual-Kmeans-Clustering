# Manual-Kmeans-Clustering

This program implements the K-means clustering algorithm without built in functions implementing raw K-Means algorithm of how actually K-Means work in the backend. The program clusters the data into K=2 groups and visualizes the clusters using a scatter plot with different colors for each cluster.

## Dataset

The dataset is read from an Excel file (`Data.csv`) using the pandas library. Make sure the file path is correctly specified in the code.

## Algorithm

The K-means clustering algorithm is implemented using the provided code. The algorithm follows these steps:

1. Initialize the centroids for the clusters.
2. Assign each data point to the nearest centroid based on the Euclidean distance.
3. Calculate the mean of the points in each cluster and update the centroids.
4. Repeat steps 2 and 3 until the centroids no longer change.

## Screenshots

![image](https://github.com/SaadARazzaq/Manual-Kmeans-Clustering/assets/123338307/fa7b9fbc-b585-4298-9b8f-c5f38f982291)

## Dependencies

- Python 3.x
- Pandas
- Matplotlib

Please ensure you have these dependencies installed before running the program.

## Usage

1. Make sure the `Data.csv` file is in the same directory as the script, or specify the correct file path in the code.
2. Run the script using Python.
3. The program will perform K-means clustering on the dataset and display the scatter plot with the clusters.

```bash
python main.py
