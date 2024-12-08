import tkinter as tk
from tkinter import ttk
import mp3_processing
import threading


class HomeTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Add Home tab components
        label = tk.Label(self, text="Paste Youtube URL:  ", font=("Helvetica", 20))
        label.pack(pady=5)

        sub_label = tk.Label(self, text="Do not use playlists!!!", font=("Helvetica", 10))
        sub_label.pack(pady=0)

        url_frame = tk.Frame(self)
        url_frame.pack(pady=5)

        url_label = tk.Label(url_frame, text="URL:", font=("Helvetica", 12))
        url_label.pack(side=tk.LEFT, padx=5)

        self.url_entry = tk.Entry(url_frame, width=50)
        self.url_entry.pack(side=tk.LEFT, padx=5)

        button = tk.Button(self, text="Download", command=self.start_download)
        button.pack(pady=10)

        #download status label: 
        self.download_label = tk.Label(self, text= "", font=("Helvetica", 12))
        self.download_label.pack(pady=5)

        # Additional metadata fields
        frame = tk.Frame(self)
        frame.pack(pady=10)

        label_artist = tk.Label(frame, text="Artist:", font=("Helvetica", 12))
        label_artist.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.text_box_artist = tk.Text(frame, height=1, width=40)
        self.text_box_artist.grid(row=0, column=1, padx=5, pady=5)

        label_album = tk.Label(frame, text="Album:", font=("Helvetica", 12))
        label_album.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        self.text_box_album = tk.Text(frame, height=1, width=40)
        self.text_box_album.grid(row=1, column=1, padx=5, pady=5)

        label_title = tk.Label(frame, text="Title:", font=("Helvetica", 12))
        label_title.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.text_box_title = tk.Text(frame, height=1, width=40)
        self.text_box_title.grid(row=2, column=1, padx=5, pady=5)

        #save button: 
        button = tk.Button(self, text="SAVE", command=self.save_song)
        button.pack(pady=10)


    def start_download(self): 
        self.download_label.config(text="DOWNLOADING...", fg="purple")
        thread = threading.Thread(target=self.download, daemon=True)
        thread.start()

    def download(self):
        #Download file to tmp location
        # Change message to indicate the download is starting
        self.download_label.config(text="DOWNLOADING...", fg="purple")
        try: 
            self.download_label.config(text="DOWNLOADING...", fg="purple")
            url_txt = self.url_entry.get()
            mp3_object  = mp3_processing.download_mp3(url_txt)
            self.download_label.config(text="DOWNLOAD SUCCESSFUL", fg="green")
            self.update_song_details(mp3_object )
        except Exception as e: 
            self.download_label.config(text=f"DOWNLOAD FAILED: {e}", fg="red")

    def update_song_details(self, mp3_object): 
        # Clear the existing content
        self.text_box_artist.delete("1.0", tk.END)
        self.text_box_album.delete("1.0", tk.END)
        self.text_box_title.delete("1.0", tk.END)

    # Insert the new metadata
        self.text_box_artist.insert("1.0", mp3_object.artist)
        self.text_box_album.insert("1.0", mp3_object.album)
        self.text_box_title.insert("1.0", mp3_object.title)

    def save_song(self):
        # Retrieve the text content from the text boxes
        title = self.text_box_title.get("1.0", "end-1c").strip()
        artist = self.text_box_artist.get("1.0", "end-1c").strip()
        album = self.text_box_album.get("1.0", "end-1c").strip()

        try:
            # Call the rename_mp3_metadata function with the retrieved values
            mp3_processing.rename_mp3_metadata(title, artist, album)
            mp3_processing.move_mp3(title, artist, album)
            self.download_label.config(text="Metadata saved successfully", fg="green")
        except Exception as e:
            self.download_label.config(text=f"Failed to save metadata: {e}", fg="red")
