import tkinter as tk
from tkinter import ttk
from home_tab import HomeTab
from settings_tab import SettingsTab

class MP3ExtractorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MP3 Extractor")
        self.geometry("800x500")

        # Create a notebook for tabs
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Add the Home tab
        home_tab = HomeTab(notebook)
        notebook.add(home_tab, text="Home")

        # Add the Settings tab
        settings_tab = SettingsTab(notebook)
        notebook.add(settings_tab, text="Settings")


if __name__ == "__main__":
    app = MP3ExtractorApp()
    app.mainloop()