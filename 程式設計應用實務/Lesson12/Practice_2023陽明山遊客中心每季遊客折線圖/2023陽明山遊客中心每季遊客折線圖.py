import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import pandas as pd

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

data = pd.read_csv("歷年國內主要觀光遊憩據點遊客人數月別統計.csv")
museum = data[
    (data['細分'] == "陽明山遊客中心") &
    (data['年別'] == 2020)]

x = ['第-季', '第二季', '第三季', '第四季']
month = museum.columns[6:-1]
y = []
for index in range(0,12,3):
    y.append(museum.iloc[0, 6+index:9+index].sum())
    print(museum.iloc[0, 6+index:9+index].sum())
# plt.plot(x, y)
# plt.title("國立自然科學博物館2023每季遊客人數")
# plt.xlabel("季別")
# plt.ylabel("遊客人數")
# plt.grid(True)
# plt.savefig("國立自然科學博物館2023每季遊客人數.png")
