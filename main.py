import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data.csv") # Can be Xlsx file
data = data.values.tolist()

def euclidean_distance(a, b):
    return (sum([(a[i] - b[i])**2 for i in range(len(a))]))** 0.5  # for sqrt

def k_means(data, k):
    centroids = [[15, 20], [17, 12]]
    assignments = [0] * len(data)

    while True:
        # Assign points to the nearest centroid
        for i, point in enumerate(data):
            assignments[i] = min(range(k), key=lambda j: euclidean_distance(point, centroids[j]))

        # Calculate the mean of the points in each cluster and update the centroids
        new_centroids = [[0, 0] for _ in range(k)]
        counts = [0] * k

        for i, point in enumerate(data):
            for j in range(2):
                new_centroids[assignments[i]][j] += point[j]
            counts[assignments[i]] += 1

        for i in range(k):
            for j in range(2):
                new_centroids[i][j] /= counts[i]

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids, assignments

def visualize_clusters(data, centroids, assignments):
    data_x, data_y = zip(*data)
    centroid_x, centroid_y = zip(*centroids)

    plt.scatter(data_x, data_y, c=assignments, cmap='viridis')
    plt.scatter(centroid_x, centroid_y, c='red', marker='x', s=100)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('K-means Clustering')
    plt.show()

k = 2
centroids, assignments = k_means(data, k)
visualize_clusters(data, centroids, assignments)
