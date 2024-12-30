import requests
import json
import pandas as pd

# 取得資料
movement_url = "https://datacenter.taichung.gov.tw/swagger/OpenData/a8dcd9fc-37f0-4d2e-be6f-edf59d16cec9"
fixed_url = "https://datacenter.taichung.gov.tw/swagger/OpenData/a3a7f779-7c2e-44cd-825d-9026805e4070"

movement_res = requests.get(movement_url)
fixed_res = requests.get(fixed_url)

movement_json = json.loads(movement_res.text)
fixed_json = json.loads(fixed_res.text)

# 提取資料
def extract_data(json_data, is_fixed):
    data_list = []
    for item in json_data:
        record = {
            "編號": item.get("編號", ""),
            "行政區": item.get("行政區", ""),
            "設置地點": item.get("設置地點", ""),
            "取締項目": item.get("取締項目", ""),
            "速限speed": item.get("速限Speed", item.get("速限speed", "")),
            "緯度": item.get("緯度", ""),
            "經度": item.get("經度", ""),
            "固定式": "是" if is_fixed else "否",
            "轄區分局": "",
            "取締行向": ""
        }
        data_list.append(record)
    return data_list

movement_data = extract_data(movement_json, is_fixed=False)
fixed_data = extract_data(fixed_json, is_fixed=True)

# 合併資料
combined_data = fixed_data + movement_data

# 轉為 DataFrame
df = pd.DataFrame(combined_data)

# 儲存為 CSV 格式
df.to_csv("combined_data.csv", index=False, encoding="utf-8-sig")

print("資料已成功儲存為 combined_data.csv。")