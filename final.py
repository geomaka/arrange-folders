import os
import json
import shutil

def organize_downloads_from_json(json_file, downloads_folder):
    with open(json_file, "r", encoding="utf-8") as f:
        folder_structure = json.load(f)

    for subfolder, files in folder_structure.items():
        for file_name in files:
            file_path = os.path.join(downloads_folder, file_name)

            if os.path.isfile(file_path):
                target_folder = os.path.join(downloads_folder, subfolder)
                
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, file_name))
                print(f"Moved '{file_name}' to '{target_folder}'")
            else:
                print(f"File '{file_name}' not found in Downloads")

if __name__ == "__main__":
    json_file = "folder_structure.json"

    downloads_folder = r"C:/Users/USER/Downloads"

    organize_downloads_from_json(json_file, downloads_folder)
