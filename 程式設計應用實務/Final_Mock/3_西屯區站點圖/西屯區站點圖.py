"""導入模組"""
import folium
import requests, json
import pandas as pd

"""取得臺中市公共自行車租借站&即時車位資料"""
res = requests.get("https://datacenter.taichung.gov.tw/swagger/OpenData/86dfad5c-540c-4479-bb7d-d7439d34eeb1")
youbike_json = json.loads(res.text)

"""提取數據"""
youbike_stations = youbike_json["retVal"]

"""轉為DataFrame"""
df = pd.DataFrame(youbike_stations)

"""篩選條件"""
xituan_stations = df[df['sarea'] == "西屯區"]

"""轉換數據類型"""
xituan_stations['lat'] = xituan_stations['lat'].astype(float)
xituan_stations['lng'] = xituan_stations['lng'].astype(float)
xituan_stations['sbi'] = xituan_stations['sbi'].astype(int)

"""定義經緯度"""
fcu_location = [24.17912418152435, 120.6470844648072]

"""創建地圖"""
map = folium.Map(location=fcu_location, zoom_start=15)

"""添加條件標記"""
for _, station in xituan_stations.iterrows():
    """顏色條件"""
    if station['sbi'] > 5:
        color = 'green'
    elif station['sbi'] > 0:
        color = 'yellow'
    else:
        color = 'red'

    """添加標記"""
    folium.CircleMarker( # 圓形標記
        location = [station['lat'], station['lng']], # 標記位置
        popup = f"{station['sna']}<br>可借車輛: {station['sbi']}", # 站點名稱和可借數量
        color = color, # 邊框顏色
        fill = True, # 是否填充
        fill_color = color, # 填充顏色
        fill_opacity = 0.7 # 填充透明度
    ).add_to(map)

"""儲存地圖"""
map.save("xituan_bike_map.html")