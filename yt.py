import yt_dlp  
import ai_summarizer
import pandas as pd 
import csv 
from yt_dlp import YoutubeDL
import ai_summarizer

def download_mp3(url):    
    save_path = '/home/curtiswiser/mp3_converter/downloads/tmp_files/tmp_mp3.%(ext)s' 
    
    print(save_path)

    # Download options
    ydl_opts = {
        'format': 'bestaudio/best',  # Choose the best audio format
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': save_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Perform the download

def extract_metadata(url):
    with yt_dlp.YoutubeDL() as ydl:
        # Extract video info (without downloading)
        info_dict = ydl.extract_info(url, download=False)
        # Attempt to extract the artist name (depends on video metadata)
        artist_name = info_dict.get('artist', None)  # Try to get the 'artist' field
        if artist_name:
            print(f"Artist: {artist_name}")
        else:
            print("Artist name not found.")
        # You can also extract other metadata such as the title, album, etc.
        video_title = info_dict.get('title', 'Unknown Title')
        return f"Title: {video_title}"
    
def download_mp3_and_save_metadata(playlist_url, csv_path):
    # Template for saving MP3 files
    save_path_template = 'downloads/tmp_files/%(title)s.%(ext)s'
    
    # List to store metadata
    metadata_list = []

    # Options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio using FFmpeg
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # Set quality
        }],
        'outtmpl': save_path_template,  # File path template
        'quiet': True,  # Suppress output
    }

    with YoutubeDL(ydl_opts) as ydl:
        # Extract playlist info without downloading (to get metadata)
        playlist_info = ydl.extract_info(playlist_url, download=False)
        
        # Handle playlists and individual videos
        if 'entries' in playlist_info:  # It's a playlist
            entries = playlist_info['entries']
        else:  # It's a single video
            entries = [playlist_info]

        # Process each entry
        for entry in entries:
            video_title = entry.get('title', 'Unknown Title')
            video_description = entry.get('description', 'No Description')
            video_id = entry.get('id')
            track_id = entry.get('playlist_index', None)  # Playlist index

            # Generate the file path based on the template
            file_path = save_path_template.replace('%(title)s', video_title).replace('%(ext)s', 'mp3')

            # Append metadata to the list
            metadata_list.append({
                'Track ID': track_id,
                'Title': video_title,
                'Description': video_description,
                'File Path': file_path,
            })

            # Download the MP3 for the video
            ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

    # Write metadata to a CSV file
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Track ID', 'Title', 'Description', 'File Path']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()  # Write column headers
        writer.writerows(metadata_list)  # Write metadata rows


