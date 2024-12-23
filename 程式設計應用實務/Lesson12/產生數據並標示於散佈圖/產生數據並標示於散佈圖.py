import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

x_data = np.random.random(10)
y_data = np.random.random(10)

plt.scatter(x_data, y_data, color="red")
plt.show()