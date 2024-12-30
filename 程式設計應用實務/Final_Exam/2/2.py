import requests
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

"""導入字型"""
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

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
            "行政區": item.get("行政區", ""),
            "固定式": "是" if is_fixed else "否"
        }
        data_list.append(record)
    return data_list

movement_data = extract_data(movement_json, is_fixed=False)
fixed_data = extract_data(fixed_json, is_fixed=True)

# 合併資料
combined_data = fixed_data + movement_data

# 轉為 DataFrame
df = pd.DataFrame(combined_data)

# 計算各行政區設備數量
fixed_counts = df[df["固定式"] == "是"]["行政區"].value_counts()
movement_counts = df[df["固定式"] == "否"]["行政區"].value_counts()

# 合併數據以便繪圖
all_districts = sorted(set(fixed_counts.index).union(set(movement_counts.index)))
data = {
    "行政區": all_districts,
    "固定式": [fixed_counts.get(district, 0) for district in all_districts],
    "移動式": [movement_counts.get(district, 0) for district in all_districts]
}
data_df = pd.DataFrame(data)

# 繪製長條圖
x = range(len(data_df))
width = 0.4

plt.bar([i - width / 2 for i in x], data_df["固定式"], width=width, color="blue", label="固定式")
plt.bar([i + width / 2 for i in x], data_df["移動式"], width=width, color="orange", label="移動式")

plt.title("台中市各行政區設備數量 (固定式 vs 移動式)")
plt.xlabel("行政區")
plt.ylabel("設備數量")
plt.xticks(x, data_df["行政區"], rotation=45)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
