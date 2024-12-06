import tkinter as tk
from tkinter import ttk


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

        button = tk.Button(self, text="Download", command=self.download)
        button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self, mode="determinate", length=300)
        self.progress_bar.pack(pady=5)

        self.progress_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.progress_label.pack(pady=5)

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

    def download(self):
        # Placeholder for download functionality
        print("Download started!")
