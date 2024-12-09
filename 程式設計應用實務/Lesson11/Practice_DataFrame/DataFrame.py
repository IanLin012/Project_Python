import pandas as pd

df = pd.read_csv('grade.csv')

science = 0

for index, row in df.iterrows():
    print(index, row['Name'], row['English'])
    science += row['Science']
    
print("Science average is", science/(index+1))