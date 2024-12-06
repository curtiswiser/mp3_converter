import json 
import os 

settings_file = 'settings.json' 

def load_settings(): 
    if not os.path.exists(settings_file): 
        return {}

    with open(settings_file, "r") as file: 
        return json.load(file)
    
def save_settings(settings): 
    with open(settings_file,"w") as file: 
        json.dump(settings, file, indent= 4)