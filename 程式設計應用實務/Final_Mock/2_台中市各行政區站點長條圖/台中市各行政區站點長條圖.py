import requests, json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

"""導入字型"""
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

"""取得資料"""
res = requests.get("https://datacenter.taichung.gov.tw/swagger/OpenData/86dfad5c-540c-4479-bb7d-d7439d34eeb1")
youbike_json = json.loads(res.text)

"""從retVal提取資料"""
youbike_stations = youbike_json["retVal"]

"""JSON轉為DataFrame"""
df = pd.DataFrame(youbike_stations)

"""選取欄位"""
df = df[['sarea']]
station_count = df['sarea'].value_counts() # 計算各行政區站點數量

"""生成長條圖"""
x = station_count.index
y = station_count.values
plt.bar(x, y)
plt.title("台中市各行政區站點統計圖")
plt.xlabel("行政區")
plt.ylabel("站點數量")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()