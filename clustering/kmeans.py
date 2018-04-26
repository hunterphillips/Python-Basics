# K-Means Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values
y = dataset.iloc[:, 3].values

# Use the elbow method to find optimal # of clusters
from sklearn.cluster import KMeans
  # Compute within-cluster sum of squares for 10 different numbers of clusters
  # store sums in array of values
wcss = []
for i in range(1, 11):
    # fit KMeans algorithm to X, set number of clusters as iterable
    kmeans = KMeans(n_clusters=i, init='k-means++',
                    n_init=10, max_iter=300, random_state=0)
    kmeans.fit(X)
    # calc sum with inertia method and append tp wcss
    wcss.append(kmeans.inertia_)
  # display chart to visualize 'elbow'
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Apply KMeans to dataset with optimal # of clusers
kmeans = KMeans(n_clusters=5, init='k-means++',n_init=10, max_iter=300, random_state=0)
  # use fit predict to return predicted cluster for each observation
y_kmeans = kmeans.fit_predict(X)


# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=50, c='red', label='Frugal')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=50, c='blue', label='Standard')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=50, c='green', label='Target')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=50, c='cyan', label='Spendthrift')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=50, c='magenta', label='Economy')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
