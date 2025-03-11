import numpy as np
from sklearn import datasets
from sklearn.datasets import fetch_openml

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import graphviz
from sklearn.tree import plot_tree

# 讀取資料
#boston = datasets.load_boston()
boston = fetch_openml(name='boston', version=1, as_frame=True)
#print(boston.feature_names)

X = (boston.data).astype(np.float32)
Y = (boston.target).astype(np.float32)
#print(X.iloc[0])
#print(Y.iloc[0])

# 資料切割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
#print(len(X_train))
#print(len(Y_train))
#print(len(X_test))
#print(len(Y_test))

# 定義模型
boston_model = LinearRegression()

# 訓練模型
boston_model.fit(X_train, Y_train)

# 模型預測
Y_predict = boston_model.predict(X_test)

plt.plot(Y_test.values, label='Real Price')
plt.plot(Y_predict, label='Predict Price')
plt.legend()
plt.show()

# 評估模型
print("R2 Score: ", r2_score(Y_test, Y_predict))
print("MSE: ", mean_squared_error(Y_test, Y_predict))

print("=============================================================")

iris = datasets.load_iris()
#print(iris.feature_names)
#print(iris.target_names)

X = iris.data
Y = iris.target
#print(X)
#print(Y)

# 資料切割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# 定義模型
decision_tree_model = DecisionTreeClassifier(criterion='entropy')

# 訓練模型
decision_tree_model.fit(X_train, Y_train)

# 模型預測
Y_predict = decision_tree_model.predict(X_test)

# 評估模型
score = accuracy_score(Y_test, Y_predict)
print("Accuracy Score: ", score)

#dot_data = export_graphviz(decision_tree_model, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True)
#graph = graphviz.Source(dot_data)
#graph.view()
plt.figure(figsize=(12, 8))
plot_tree(decision_tree_model, 
          feature_names=iris.feature_names, 
          class_names=iris.target_names, 
          filled=True, rounded=True)
plt.show()
