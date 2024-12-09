import requests, json
import pandas as pd

response = requests.get("https://opendata.taichung.gov.tw/search/c8c10867-0ff6-4adb-b8af-bc6ea19357bb")
traffic_json = json.loads(response.text)
#print(traffic_json)

df = pd.DataFrame(traffic_json)
print(df)

excel_writer = pd.ExcelWriter('112年11月台中市交通事故資料.xlsx')

for area in "區":
    station_df = df[df['區'] == area]
    station_df.to_excel(excel_writer, sheet_name=area)

excel_writer.close()