import yt_dlp  
import ai_summarizer


def download_mp3(url, path):
    link = "https://www.youtube.com/watch?v=bZwxTX2pWmw"
    save_path = '/home/curtiswiser/mp3_converter/downloads/%(title)s.%(ext)s' 
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
        ydl.download([link])  # Perform the download

def extract_metadata(link):
    with yt_dlp.YoutubeDL() as ydl:
        # Extract video info (without downloading)
        info_dict = ydl.extract_info(link, download=False)
        # Attempt to extract the artist name (depends on video metadata)
        artist_name = info_dict.get('artist', None)  # Try to get the 'artist' field
        if artist_name:
            print(f"Artist: {artist_name}")
        else:
            print("Artist name not found.")
        # You can also extract other metadata such as the title, album, etc.
        video_title = info_dict.get('title', 'Unknown Title')
        print(f"Title: {video_title}")