from yt_dlp import YoutubeDL

option = {'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"}
ydl = YoutubeDL(option)
ydl.download(input("Enter the URL: "))
