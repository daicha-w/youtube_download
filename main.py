from yt_dlp import YoutubeDL

option = {'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]", 'outtmpl': "./out/%(title)s.%(ext)s"}
ydl = YoutubeDL(option)
ydl.download(input("Enter the URL: "))
