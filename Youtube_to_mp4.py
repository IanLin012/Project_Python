import os # 作業系統相關模組(常用於檔案複製、修改、查詢)
os.chdir('C:\\Users\\drlin\\Desktop\\012') # 改變工作目錄到指定的路徑

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=404OiMAu6aY&ab_channel=FashionProX')
print('Downloading...')
yt.streams.filter().get_by_resolution('1080p').download() # 下載固定畫質影片，以filename為檔名
print('Download successful !')
