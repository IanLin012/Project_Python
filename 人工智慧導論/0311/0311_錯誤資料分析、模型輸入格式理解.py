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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5)

"""Random Forest"""
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, Y_train)

rf_pred = random_forest.predict(X_test)
rf_accuracy = accuracy_score(Y_test, rf_pred)
print("Random Forest accuracy: ", rf_accuracy)

print("------------------------------------")

"""KNN"""
knn = KNeighborsClassifier(n_neighbors=20)
knn.fit(X_train, Y_train)

knn_pred = knn.predict(X_test)
knn_accuracy = accuracy_score(Y_test, knn_pred)
print("KNN accuracy", knn_accuracy)

plt.figure(figsize=(6, 6))
colmap = np.array(['blue', 'green', 'red'])
plt.scatter(X_test[:, 0], X_test[:, 1], c=colmap[Y_test], s=100, marker='o', alpha=0.5)
plt.scatter(X_test[:, 0], X_test[:, 1], c=colmap[knn_pred], s=50, marker='x', alpha=0.5)
plt.xlabel('Sepal Length ')
plt.ylabel('Sepal Width ')
plt.show()

print("------------------------------------")

X, _ = make_blobs(n_samples=300, centers=10, random_state=1)
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], s=50, marker='x', alpha=0.5)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Generated Dataset')
plt.show()

"""K-Means"""
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

kmeans_pred = kmeans.predict(X)
plt.figure(figsize=(6, 6))
colmap = np.array(['blue', 'green', 'red'])
plt.scatter(X[:, 0], X[:, 1], c=colmap[kmeans_pred], s=30, marker='x')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.75, marker='o')
plt.show()

"""
1. 自訂一筆資料丟給模型進行預測
2. 在測試集的資料找出以下:
分類錯誤的是第幾筆
錯誤的內容是什麼?
"""
data = np.array([[1, 2, 3, 4]])
data_pred = knn.predict(data)
print(data_pred)

missclass = np.where(Y_test != knn_pred)[0]
print(missclass)

print(len(X_test))

missclass_X = X_test[missclass]
missclass_Y = Y_test[missclass]
missclass_pred = knn_pred[missclass]

for i in range(len(missclass)):
    print("樣本資料:", missclass_X[i], "真實分類", missclass_Y[i], "預測結果", missclass_pred[i])
