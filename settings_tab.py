import tkinter as tk
from tkinter import filedialog 
import settings


class SettingsTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #load existing settings:
        self.settings = settings.load_settings()

        # Add Settings tab components
        settings_label = tk.Label(self, text="Settings", font=("Helvetica", 20))
        settings_label.pack(pady=10)

        # Default path input
        path_label = tk.Label(self, text="Default Download Path:", font=("Helvetica", 12))
        path_label.pack(anchor="w", padx=10)

        #frame for the folder pkcr bttton: 
        path_frame = tk.Frame(self)
        path_frame.pack(padx=10, pady=5, fill= tk.X)

        self.path_entry = tk.Entry(path_frame, width= 50)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand= True, padx= 5)
        self.path_entry.insert(0, self.settings.get("download_path", ""))

        #add function to browser button 
        browse_button = tk.Button(path_frame, text='Browse', command=self.pick_folder)
        browse_button.pack(side=tk.RIGHT, padx=5)

        # Auto rename checkbox
        self.ai_suggestion = tk.BooleanVar(value=self.settings.get("Enable_AI", False))

        ai_suggestion = tk.Checkbutton(
            self, text="Enable AI Naming Suggestions", variable=self.ai_suggestion
        )
        ai_suggestion.pack(anchor="w", padx=10, pady=5)

        # Frame for API Key label and entry
        api_frame = tk.Frame(self)
        api_frame.pack(pady=10, padx=10, anchor="w")  # Adjusts the layout and alignment

        # API Key label
        api_label = tk.Label(api_frame, text="API Key:", font=("Helvetica", 12))
        api_label.pack(side=tk.LEFT, padx=5)

        # API Key entry box
        self.api_key_entry = tk.Entry(api_frame, width=100) 
        self.api_key_entry.pack(side=tk.LEFT, padx=5)
        self.api_key_entry.insert(0, self.settings.get("api_key", ""))  # Load saved API key

        # Save button
        save_button = tk.Button(self, text="Save Settings", command=self.save_settings)
        save_button.pack(pady=10)

        # Message label
        self.message_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=5)

    def save_settings(self):
        """Save current settings to the settings file."""
        self.settings["download_path"] = self.path_entry.get()
        self.settings["api_key"] = self.api_key_entry.get()
        self.settings["Enable_AI"] = self.ai_suggestion.get()

        try:
            settings.save_settings(self.settings)
            self.message_label.config(text="Settings saved successfully!", fg="green")
        except Exception as e:
            self.message_label.config(text=f"Error saving settings: {e}", fg="red")

    def pick_folder(self):
        # Open a folder picker dialog and set the result in the entry
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_selected)