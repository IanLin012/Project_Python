import pandas as pd

data = pd.read_csv('Project_Python\\2025_Route_Geometry\\202501_combined_congestion.csv')

#filter_values = ["03F2066S" ,"03F2079S" ,"03F2066N" ,"03F2078N" ,"03F2100S" ,"03F2129S" ,"03F2100N" ,"03F2125N" ,"03F2152S" ,"03F2194S" ,"03F2153N" ,"03F2194N"]
#filtered_df = df[df.iloc[:, 1].isin(filter_values) & df.iloc[:, 2].isin(filter_values)]

#filtered_data = data[data['Speed'] < 80]

filtered_data = (
    data
    .groupby(['GantryFrom', 'GantryTo', 'VehicleType'], as_index=False)
    .apply(lambda group: pd.DataFrame({
        'GantryFrom': [group['GantryFrom'].iloc[0]],
        'GantryTo': [group['GantryTo'].iloc[0]],
        'VehicleType': [group['VehicleType'].iloc[0]],
        'Speed': [(group['Speed'] * group['Volume']).sum() / group['Volume'].sum()],
        'Volume': [group['Volume'].sum()]  # 總量
    }))
    .reset_index(drop=True)  # 移除多餘的索引
)

filtered_data.to_csv('Project_Python\\2025_Route_Geometry\\202501_combined_congestion_weighted.csv', index=False, header=True)
