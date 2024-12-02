import yt 
import ai_summarizer
import json
from mutagen.easyid3 import EasyID3
import shutil
import os
import pandas as pd 

def convert_to_json(data): 
    data = data.replace('`','')
    data = data.replace('json','')
    data = data.replace('[','')
    data = data.replace(']','')
    data = data.strip()
    return json.loads(data)




def process_urls(url): 
    #download tmp file: 
    yt.download_mp3(url=url)

    #get metadata for mp3 file
    url_description = yt.extract_metadata(url)
    print(url_description)

    #summarize artist info
    data = ai_summarizer.get_mp3_details(description=url_description)
    #convert to json
    json_data = convert_to_json(data)

    # # Load the MP3 file
    audio = EasyID3("downloads/tmp_files/tmp_mp3.mp3")

    # Edit metadata
    try: 
        audio["title"] = json_data.get('song')
    except:
        print(f"Error setting title tag")
    try: 
        audio["artist"] = json_data.get('artist') 
    except:
        print(f"Error setting artist tag")
    try: 
        audio["album"] = json_data.get('album') 
    except: 
        print(f"Error setting album tag")

    # # Save the changes
    audio.save()

    # Explicitly close the file handle (though EasyID3 should manage this)
    audio = None 

    # New file name based on the title
    title = json_data['song']
    new_file_name = f"{title}.mp3"

    # Replace characters not allowed in filenames
    valid_file_name = "".join(c if c.isalnum() or c in " ._-" else "_" for c in new_file_name)

    # Target path in the Downloads folder
    artist = json_data.get('artist') 
    album = json_data.get('album') 

    print(f'Artist: {artist}')
    print(f'Album: {album}')
    print(f'Song: {title}')

    downloads_folder = f"downloads/music/{artist}/{album}"
    target_path = os.path.join(downloads_folder, valid_file_name)
    # Create the directories if they don't exist
    os.makedirs(downloads_folder, exist_ok=True)
    # Move and rename the file
    shutil.move("downloads/tmp_files/tmp_mp3.mp3", target_path)

    print(f"File moved and renamed to: {target_path}")



def main():
    df = pd.read_csv('playlist_metadata.csv')

    for index, row in df.iterrows(): 
        
        url = row['YouTube URL:']
        processed = row['processed']

        if processed == "N": 
            print('-----------------------------------------------------------------------------------------------------')
            print(f"Current Link: {url}")
            process_urls(url)

            df.at[index, 'processed'] = "Y"

    # Save the updated DataFrame back to the CSV
    df.to_csv('playlist_metadata.csv', index=False)


main()