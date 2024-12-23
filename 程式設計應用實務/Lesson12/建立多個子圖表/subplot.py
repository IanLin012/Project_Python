import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

data = pd.read_csv("sales_data.csv")
x=data['Price']
y=data['Sales']
figure = plt.figure()

plt.figure(figsize=(10,20))

plt.subplot(141)
plt.scatter(x, y)
plt.subplot(142)
plt.scatter(x, y)
plt.subplot(143)
plt.scatter(x, y)
plt.subplot(144)
plt.scatter(x, y)
plt.savefig("t.png")
plt.show()
plt.close()