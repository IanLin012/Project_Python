import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

dataset = pd.read_csv('Project_Python\\人工智慧導論\\0225\\linear_regression_Yearssalary.csv')

X = dataset.iloc[:, 1].values.reshape(-1, 1)
Y = dataset.iloc[:, 2]
#print(Y)

#plt.scatter(X, Y)
#plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
#print(len(X_train))
#print(len(X_test))


# 定義模型
regressor = LinearRegression()

# 訓練模型
regressor.fit(X_train, Y_train)

# 模型預測
Y_predict = regressor.predict(X_test)
#print(Y_predict)
#print("=============================================================")
#print(Y_test)

# 評估模型測試集
score =  r2_score(Y_test, Y_predict)
print(score)

# 評估模型訓練集
Y_predict = regressor.predict(X_train)
score = r2_score(Y_train, Y_predict)
print(score)

# 模型與訓練集的關聯
plt.scatter(X_train, Y_train, color='red')
plt.scatter(X_test, Y_test, color='green')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Years (Training set)')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()
"""
# 模型與測試集的關聯
plt.scatter(X_test, Y_test, color='red')
plt.plot(X_test, regressor.predict(X_test), color='blue')
plt.title('Salary vs Years (Training set)')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()
"""
#a = regressor.intercept_
#b = regressor.coef_
#print('Interception截距(a): ', a)
#print('Coeficientv係數(b): ' , b)

## y(年資) = 22302 * x(年貸) + 4077
# 模型認為的表達方式
# y = ax + b
# a  = 22302
# b = 4077

print("======================================================================")

# 定義模型
regress_poly = make_pipeline(PolynomialFeatures(degree=4), LinearRegression())

# 訓練模型
regress_poly.fit(X_train, Y_train)

# 模型預測
Y_predict = regress_poly.predict(X_test)

# 評估模型
score = r2_score(Y_test, Y_predict) 
print(score)

# 訓練集排序
sort_train = sorted(zip(X_train, Y_train))
X_train, Y_train = zip(*sort_train)

# 測試集排序
sort_test = sorted(zip(X_test, Y_test))
X_test, Y_test = zip(*sort_test)

#模型與訓練集的關聯
plt.scatter(X_train, Y_train, color='red')
plt.scatter(X_test, Y_test, color='green')
plt.plot(X_train, regress_poly.predict(X_train), color='blue')
plt.title('Salary vs Learning Hours (Training set)')
plt.xlabel('Hours of Learning per Month')
plt.ylabel('Salary')
plt.show()
"""
# 模型與測試集的關聯
plt.scatter(X_test, Y_test, color='red')
plt.plot(X_test, regress_poly.predict(X_test), color='blue')
plt.title('Salary vs Learning Hours (Training set)')
plt.xlabel('Hours of Learning per Month')
plt.ylabel('Salary')
plt.show()
"""