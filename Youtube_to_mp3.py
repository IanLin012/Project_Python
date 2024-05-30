import os
os.chdir('C:\\Users\\drlin\\Music')

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=ZsbaD7-4bgc&ab_channel=JJLin%E6%9E%97%E4%BF%8A%E5%82%91', use_oauth=True, allow_oauth_cache=True)
print('Downloading...')
yt.streams.filter().get_audio_only().download(filename='裹著心的光.mp3')
print('Download successful!')