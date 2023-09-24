import os # 作業系統相關模組(常用於檔案複製、修改、查詢)
os.chdir('C:\\Users\\drlin\\Music\\林俊傑') # 改變工作目錄到指定的路徑

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=u9ol8et8laQ&ab_channel=%E9%BA%92%E9%BA%9F%E5%85%92%E9%9F%B3%E6%A8%82', use_oauth=True, allow_oauth_cache=True)
print('Downloading...')
yt.streams.filter().get_audio_only().download(filename='Castle In The Air 林俊傑.mp3') # 下載音檔，以filename做為檔名
print('Download successful!')
