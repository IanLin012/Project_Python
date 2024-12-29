import requests, json
import pandas as pd

"""取得資料"""
res = requests.get("https://datacenter.taichung.gov.tw/swagger/OpenData/86dfad5c-540c-4479-bb7d-d7439d34eeb1")
youbike_json = json.loads(res.text)

"""從retVal提取資料"""
youbike_stations = youbike_json["retVal"]

"""JSON轉為DataFrame"""
df = pd.DataFrame(youbike_stations)

"""篩選西屯區資料"""
xitun_data = df[df['sarea'] == "西屯區"]

xitun_data.to_csv("xitun_youbike.csv")

data = pd.read_csv("xitun_youbike.csv")
print(data)