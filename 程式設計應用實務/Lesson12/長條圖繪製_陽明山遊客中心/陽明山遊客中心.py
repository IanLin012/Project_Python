import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import pandas as pd

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

data = pd.read_csv("歷年國內主要觀光遊憩據點遊客人數月別統計.csv")
ym = data[data['細分'] == "陽明山遊客中心"]
print(ym.columns)

# x = ym['年別']
# y = ym['合計']
# plt.bar(x, y)
# plt.title("陽明山遊客中心2012-2023遊客人數")
# plt.xlabel("年別")
# plt.ylabel("全年遊客人數")
# plt.grid(True)
# plt.savefig("陽明山遊客中心2012-2023遊客人數.png")

x = ym.columns[6:-1]
for index, row in ym.iterrows():
    year = str(row['年別'])
    y = row[x]
    plt.bar(x, y)
    plt.title("陽明山遊客中心"+year+"年遊客人數")
    plt.xlabel("月別")
    plt.ylabel("每月遊客人數")
    plt.grid(True)
    plt.savefig("陽明山遊客中心"+year+"年遊客人數.png")
    plt.close()

plt.show()