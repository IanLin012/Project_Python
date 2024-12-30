import folium
import requests
import json
import pandas as pd

# 定位逢甲大學經緯度座標
fcu_location = [24.17912418152435, 120.6470844648072]

# 取得固定式與移動式設備資料
movement_url = "https://datacenter.taichung.gov.tw/swagger/OpenData/a8dcd9fc-37f0-4d2e-be6f-edf59d16cec9"
fixed_url = "https://datacenter.taichung.gov.tw/swagger/OpenData/a3a7f779-7c2e-44cd-825d-9026805e4070"

movement_res = requests.get(movement_url)
fixed_res = requests.get(fixed_url)

movement_json = json.loads(movement_res.text)
fixed_json = json.loads(fixed_res.text)

# 提取資料
def extract_data(json_data):
    data_list = []
    for item in json_data:
        record = {
            "行政區": item.get("行政區", ""),
            "速限speed": item.get("速限Speed", item.get("速限speed", "")),
            "緯度": item.get("緯度", ""),
            "經度": item.get("經度", "")
        }
        data_list.append(record)
    return data_list

movement_data = extract_data(movement_json)
fixed_data = extract_data(fixed_json)

# 合併資料
combined_data = pd.DataFrame(movement_data + fixed_data)

# 轉換數據類型
combined_data["速限speed"] = pd.to_numeric(combined_data["速限speed"], errors="coerce")
combined_data["緯度"] = pd.to_numeric(combined_data["緯度"], errors="coerce")
combined_data["經度"] = pd.to_numeric(combined_data["經度"], errors="coerce")

# 創建地圖
map = folium.Map(location=fcu_location, zoom_start=12)

# 添加標記
for _, row in combined_data.iterrows():
    speed = row["速限speed"]
    lat = row["緯度"]
    lng = row["經度"]

    if pd.notna(speed) and pd.notna(lat) and pd.notna(lng):
        if speed <= 50:
            color = 'green'
        elif 60 <= speed <= 70:
            color = 'yellow'
        elif speed >= 80:
            color = 'red'
        else:
            continue

        folium.CircleMarker(
            location=[lat, lng],
            popup=f"速限: {speed} km/h",
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7
        ).add_to(map)

# 添加按鈕
folium.map.LayerControl().add_to(map)

# 儲存地圖
map.save("taichung_speed_map.html")

print("地圖已成功儲存為 taichung_speed_map.html")
