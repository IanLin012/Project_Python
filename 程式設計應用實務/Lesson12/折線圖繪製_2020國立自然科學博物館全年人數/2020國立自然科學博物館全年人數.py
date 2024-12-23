import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import pandas as pd

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

data = pd.read_csv("歷年國內主要觀光遊憩據點遊客人數月別統計.csv")
museum = data[
    (data['細分'] == "國立自然科學博物館") &
    (data['年別'] == 2020)]

x = museum.columns[6:-1]
y = museum[x].iloc[0]
print(y)
plt.plot(x, y)
plt.title("國立自然科學博物館2020遊客人數")
plt.xlabel("月別")
plt.ylabel("遊客人數")
plt.grid(True)
plt.savefig("國立自然科學博物館2020遊客人數.png")
