import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# produce data
iris = datasets.load_iris()
X = iris.data
Y = iris.target
np.random.seed(42)
#print(iris.feature_names)
#print(iris.target_names)

# split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4)

# random forest
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, Y_train)

Y_pred = random_forest.predict(X_test)
random_forest_accuracy = accuracy_score(Y_test, Y_pred)
print("RF classification accuracy: ", random_forest_accuracy)

# KNN
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, Y_train)

knn_predict = knn.predict(X_test)
knn_accuracy = accuracy_score(Y_test, knn_predict)
print("KNN classification accuracy: ", knn_accuracy)

plt.figure(figsize=(6, 6))
colmap = np.array(['blue', 'green', 'red'])
plt.scatter(X_test[:, 0], X_test[:, 1], c=colmap[knn_predict], s=150, marker='o', alpha=0.5)
plt.scatter(X_test[:, 0], X_test[:, 1], c=colmap[knn_predict], s=50, marker='x', alpha=0.5)
plt.xlabel('Sepal Length ')
plt.ylabel('Sepal Width ')
plt.show()

# K-means
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1)
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], s=30, marker='X', alpha=0.6)
plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
"""
k_means_predict = kmeans.predict(X_test)
k_means_accuracy = accuracy_score(Y_test, k_means_predict)
print("K-means classification accuracy: ", k_means_accuracy)
"""
Y = kmeans.predict(X)
plt.figure(figsize=(6, 6))
colmap = np.array(['blue', 'green', 'red', 'yellow'])
plt.scatter(X[:, 0], X[:, 1], c=colmap[Y], s=30, marker='x')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()
"""
plt.scatter(X_test[:, 0], X_test[:, 1], c=colmap[k_means_predict], s=150, marker='o', alpha=0.5)
plt.scatter(X_test[:, 0], X_test[:, 1], c=colmap[k_means_predict], s=50, marker='x', alpha=0.5)
plt.xlabel('Sepal Length ')
plt.ylabel('Sepal Width ')
plt.show()
"""
