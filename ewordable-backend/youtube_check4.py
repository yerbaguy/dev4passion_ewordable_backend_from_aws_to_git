from yt_dlp import YoutubeDL

video_url = "https://www.youtube.com/watch?v=mDveiNIpqyw"
opts = dict()

with YoutubeDL(opts) as yt:
    yt.download([video_url])
