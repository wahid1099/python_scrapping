import youtube_dl
import os

# URL of the YouTube playlist
playlist_url = 'https://youtube.com/playlist?list=PLkyGuIcLcmx1mIPyMdVodlSVJqL7Y9Wv7'

# Set options for the downloader
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'folder_path/%(title)s.%(ext)s',
    'ignoreerrors': True,
}

# Create the folder if it doesn't exist
folder_path = 'myvedios'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Download the playlist using youtube_dl
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
