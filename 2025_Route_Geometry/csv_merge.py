import os
import pandas as pd

# 設定資料夾路徑
folder_path = 'Project_Python\\2025_Route_Geometry\\車速中位數'

# 獲取資料夾內所有檔案
files = [f for f in os.listdir(folder_path)]

combined_df = pd.DataFrame()

for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, header=None)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

combined_df.to_csv('Project_Python\\2025_Route_Geometry\\車速中位數\\202501_new.csv', index=False, header=False)

print("所有檔案已成功合併")