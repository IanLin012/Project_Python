import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('Project_Python\\2025_Route_Geometry\\車速中位數\\20250102.csv')

# List of values to filter the second and third columns
filter_values = ["03F2066S" ,"03F2079S" ,"03F2066N" ,"03F2078N" ,"03F2100S" ,"03F2129S" ,"03F2100N" ,"03F2125N" ,"03F2152S" ,"03F2194S" ,"03F2153N" ,"03F2194N"]

# Filter the rows where both the second and third columns contain any of the values in filter_values
filtered_df = df[df.iloc[:, 1].isin(filter_values) & df.iloc[:, 2].isin(filter_values)]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('Project_Python\\2025_Route_Geometry\\車速中位數\\20250102_new.csv', index=False, header=False)
