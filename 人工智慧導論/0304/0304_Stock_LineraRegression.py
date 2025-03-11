import numpy as np
from sklearn import datasets

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd

# 讀取資料
dataset = pd.read_csv('NVDA.csv')

X = dataset.iloc[:, 1].values.reshape(-1, 1)
Y = dataset.iloc[:, 2]

# 資料切割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# 定義模型
regression = LinearRegression()

# 訓練模型
regression.fit(X_train, Y_train)

# 模型預測
Y_predict = regression.predict(X_test)

plt.plot(Y_test.values, label='Real Price')
plt.plot(Y_predict, label='Predict Price')
plt.legend()
plt.show()