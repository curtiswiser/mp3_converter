
import ai_summarizer
from mutagen.easyid3 import EasyID3
import yt_dlp
import os 
import shutil

import settings


class mp3(): 
    def __init__(self, url):
        self.url = url  
        self.settings = settings.load_settings()
        self.ai_enabled = self.settings['Enable_AI']
        self.download_path = self.settings['download_path']
        self.song_metadata = self.extract_metadata()

        self.song_details = ai_summarizer.get_mp3_details(self.song_metadata)
        
        self.title = self.song_details.get('song', 'Unknown')
        self.artist = self.song_details.get('artist', 'Unknown')
        self.album = self.song_details.get('album', 'Unknown')

    def extract_metadata(self):
        with yt_dlp.YoutubeDL() as ydl:
            # Extract video info (without downloading)
            info_dict = ydl.extract_info(self.url, download=False)
            video_title = info_dict.get('title', 'Unknown Title')
            return f"Title: {video_title}"
        



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

    #create object: 
    return mp3(url)


def rename_mp3_metadata(title, artist, album):
    # Load settings
    all_settings = settings.load_settings()
    # Get the full path to the temporary MP3 file
    file_path = f"{all_settings['download_path']}/tmp_files/tmp_mp3.mp3"

    try:
        # Load the MP3 file
        audio = EasyID3(file_path)

        # Update the metadata
        if title:
            audio['title'] = title
        if artist:
            audio['artist'] = artist
        if album:
            audio['album'] = album

        # Save changes to the file
        audio.save()
        print(f"Metadata updated successfully for {file_path}")

    except Exception as e:
        print(f"Failed to update metadata: {e}")



def move_mp3(title, artist, album): 
    # Load settings
    all_settings = settings.load_settings()
    download_path = all_settings['download_path']
    current_file = f"{download_path}/tmp_files/tmp_mp3.mp3"

    new_file_name = f'{title}.mp3'
    # Replace characters not allowed in filenames
    valid_file_name = "".join(c if c.isalnum() or c in " ._-" else "_" for c in new_file_name)

    download_folder = f'{download_path}/{artist}/{album}'

    target_path = os.path.join(download_folder, valid_file_name)
    #create new directory if it doesn't exist: 
    os.makedirs(download_folder, exist_ok=True)
    #move and rename file: 
    shutil.copy(current_file, target_path)


    


# mp3_object  = download_mp3(url = "https://www.youtube.com/watch?v=HaC0s-FP-r4")


# print(mp3_object.title)
# print(mp3_object.artist)
# print(mp3_object.album)

    







