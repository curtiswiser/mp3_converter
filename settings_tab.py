import tkinter as tk
from tkinter import filedialog 


class SettingsTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

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

        #add function to browser button 
        browse_button = tk.Button(path_frame, text='Browse', command=self.pick_folder)
        browse_button.pack(side=tk.RIGHT, padx=5)

     
        # Auto rename checkbox
        self.auto_rename_var = tk.BooleanVar()
        auto_rename_check = tk.Checkbutton(
            self, text="Enable AI Naming Suggestions", variable=self.auto_rename_var
        )
        auto_rename_check.pack(anchor="w", padx=10, pady=5)

        # Save button
        save_button = tk.Button(self, text="Save Settings", command=self.save_settings)
        save_button.pack(pady=10)

        # Message label
        self.message_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=5)

    def save_settings(self):
        # Retrieve settings values
        default_path = self.path_entry.get()
        auto_rename = self.auto_rename_var.get()

        # Print or save the settings
        print(f"Default Path: {default_path}")
        print(f"Auto Rename: {'Enabled' if auto_rename else 'Disabled'}")
        print(auto_rename)

        # Show a confirmation message
        self.message_label.config(text="Settings saved successfully!", fg="green")

    def pick_folder(self):
        # Open a folder picker dialog and set the result in the entry
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_selected)