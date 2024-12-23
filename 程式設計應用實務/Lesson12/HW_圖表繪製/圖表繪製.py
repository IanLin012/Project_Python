import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import fontManager

"""導入字體"""
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')


"""讀取資料"""
data = pd.read_csv("歷年國內主要觀光遊憩據點遊客人數月別統計.csv")

"""篩選資料"""
museum = data[(data['細分'] == "國立自然科學博物館") & (data['年別'].between(2018, 2023))]

"""繪製2018-2023國立自然科學博物館歷月遊客人數折線圖"""
plt.figure(1)
x = museum.columns[6:-1]
y = museum[x].mean()
plt.plot(x, y)
plt.title("2018-2023國立自然科學博物館歷月遊客人數折線圖")
plt.xlabel("月別")
plt.ylabel("遊客人數")
plt.grid(True)
plt.tight_layout()

"""篩選資料"""
ym = data[data['年別'] == 2023]

"""繪製2023各類型旅遊人數長條圖"""
plt.figure(2)
x = ym['類型']
y = ym['合計']
plt.bar(x, y)
plt.title("2023各類型旅遊人數長條圖")
plt.xlabel("類型")
plt.ylabel("旅遊人數")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()


"""讀取資料"""
df = pd.read_csv("weather_data.csv")

"""創建 2x2 子圖表"""
fig, axes = plt.subplots(3, 2, figsize=(15, 5))

"""第一個子圖"""
axes[0, 0].scatter(df['Temperature'], df['Ice_Cream_Sales'], color='blue')
axes[0, 0].set_xlabel("Temperature")
axes[0, 0].set_ylabel("Ice_Cream_Sales")
axes[0, 0].set_title("Temperature vs Ice_Cream_Sales")

"""第二個子圖"""
axes[0, 1].scatter(df['Temperature'], df['Swimming_Pool_Usage'], color='blue')
axes[0, 1].set_xlabel("Temperature")
axes[0, 1].set_ylabel("Swimming_Pool_Usage")
axes[0, 1].set_title("Temperature vs Swimming_Pool_Usage")

"""第三個子圖"""
axes[1, 0].scatter(df['Temperature'], df['Cold_Drink_Sales'], color='blue')
axes[1, 0].set_xlabel("Temperature")
axes[1, 0].set_ylabel("Cold_Drink_Sales")
axes[1, 0].set_title("Temperature vs Cold_Drink_Sales")

"""第四個子圖"""
axes[1, 1].scatter(df['Ice_Cream_Sales'], df['Swimming_Pool_Usage'], color='blue')
axes[1, 1].set_xlabel("Ice_Cream_Sales")
axes[1, 1].set_ylabel("Swimming_Pool_Usage")
axes[1, 1].set_title("Ice_Cream_Sales vs Swimming_Pool_Usage")

"""第五個子圖"""
axes[2, 0].scatter(df['Ice_Cream_Sales'], df['Cold_Drink_Sales'], color='blue')
axes[2, 0].set_xlabel("Ice_Cream_Sales")
axes[2, 0].set_ylabel("Cold_Drink_Sales")
axes[2, 0].set_title("Ice_Cream_Sales vs Cold_Drink_Sales")

"""第六個子圖"""
axes[2, 1].scatter(df['Swimming_Pool_Usage'], df['Cold_Drink_Sales'], color='blue')
axes[2, 1].set_xlabel("Swimming_Pool_Usage")
axes[2, 1].set_ylabel("Cold_Drink_Sales")
axes[2, 1].set_title("Swimming_Pool_Usage vs Cold_Drink_Sales")

"""顯示散佈圖"""
plt.tight_layout() # 調整圖表間距，避免重疊
plt.show()