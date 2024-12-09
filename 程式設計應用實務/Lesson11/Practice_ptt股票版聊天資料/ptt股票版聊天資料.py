import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.ptt.cc/bbs/Stock/M.1732062670.A.6EF.html')
soup = BeautifulSoup(response.text, 'html.parser')

pushes = soup.find_all('div', class_='push')
data = []

for push in pushes:
    push_tag = push.find('span', class_='push-tag')
    push_userid = push.find('span', class_='push-userid')
    push_content = push.find('span', class_='push-content')
    push_time = push.find('span', class_='push-ipdatetime')

    if push_tag and push_userid and push_content and push_time:
        data.append({
            'Tag': push_tag.text.strip(),
            'UserID': push_userid.text.strip(),
            'Content': push_content.text.strip(': ').strip(),
            'Time': push_time.text.strip()
        })

df = pd.DataFrame(data)
df.to_csv('ptt股票版聊天資料.csv')