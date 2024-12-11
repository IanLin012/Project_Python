import requests, json
import pandas as pd

"""取得台中市112年11月交通事故資料"""
response = requests.get("https://datacenter.taichung.gov.tw/swagger/OpenData/92979089-9aaf-4ba3-be97-85e857ec4fd5")
traffic_json = json.loads(response.text)
# print(traffic_json)

"""JSON 轉為 DataFrame"""
df = pd.DataFrame(traffic_json)

"""區域分組"""
grouped = df.groupby('區')

"""每個區域儲存到不同的工作簿"""
excel_writer = pd.ExcelWriter('112年11月台中市交通事故資料.xlsx')
for area, data in grouped:
    data.to_excel(excel_writer, sheet_name=area, index=False)
excel_writer.close()

print("成功儲存資料")