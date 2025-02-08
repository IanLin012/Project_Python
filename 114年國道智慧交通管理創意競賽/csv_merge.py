import os
import pandas as pd

"""
folder_path = 'Project_Python\\2025_Route_Geometry\\車速中位數'

files = [f for f in os.listdir(folder_path)]
combined_df = pd.DataFrame()

for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, header=None)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

combined_df.to_csv('Project_Python\\2025_Route_Geometry\\車速中位數\\202501_new.csv', index=False, header=False)
"""

df1 = pd.read_csv("Project_Python\\2025_Route_Geometry\\車速中位數\\202501.csv")
df2 = pd.read_csv("Project_Python\\2025_Route_Geometry\\202501_道路幾何特性.csv")

merged = pd.concat([df1, df2], axis=1)

merged.to_csv("Project_Python\\2025_Route_Geometry\\202501_new.csv", index=False)

print("檔案已合併")