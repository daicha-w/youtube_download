from yt_dlp import YoutubeDL

option = {}

print("0: Live, 1: Video, 2: Audio")
match int(input("Enter the option: ")):
    case 0:
        option = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "outtmpl": "./out/%(title)s.%(ext)s",
            "live_from_start": "True"
        }
    case 1:
        option = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "outtmpl": "./out/%(title)s.%(ext)s"
        }
    case 2:
        option = {"format": "bestaudio[ext=m4a]", "outtmpl": "./out/%(title)s.%(ext)s"}
    case _:
        print("Error: Invalid option")
        exit()
ydl = YoutubeDL(option)
ydl.download(input("Enter the URL: "))
