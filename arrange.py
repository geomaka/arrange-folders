import os
import json

def save_folder_structure_to_json(reference_folder, output_file):
    folder_structure = {}

    for root, _, files in os.walk(reference_folder):
        rel_path = os.path.relpath(root, reference_folder)
        if rel_path == ".":
            rel_path = "Main Directory"

        folder_structure[rel_path] = files

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(folder_structure, f, indent=4)

    print(f"Folder structure saved to '{output_file}'")

if __name__ == "__main__":
    reference_folder = r"C:/Users/USER\Downloads/The Complete Cyber Security Course  Hackers Exposed!"

    output_file = "folder_structure.json"

    save_folder_structure_to_json(reference_folder, output_file)
