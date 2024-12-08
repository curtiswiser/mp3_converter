
import ai_summarizer
from mutagen.easyid3 import EasyID3
import yt_dlp
import settings


class mp3(): 
    def __init__(self, url):
        self.url = url  
        self.download_path = settings.get("download_path")
        self.enable_ai = settings.get("Enable_AI")

    def get_track_details(self): 
        json_data = ai_summarizer.get_mp3_details(self.url)
        self.title = json_data.get('song', 'Unknown')
        self.artist = json_data.get('artist', 'Unknown')
        self.album = json_data.get('album', 'Unknown')


def download_mp3(url):  
    #create a tmp file
    all_settings = settings.load_settings()

    download_path = all_settings['download_path']
    download_path = f'{download_path}/tmp_files/tmp_mp3.%(ext)s' 

    # Download options
    ydl_opts = {
        'format': 'bestaudio/best',  # Choose the best audio format
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': download_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Perform the download
    







