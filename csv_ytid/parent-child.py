import os
import json

root_folder = './val_data'  # Replace with your root folder path
folder_dict = {}

for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    
    if os.path.isdir(folder_path):
        folder_files = []
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            if os.path.isfile(file_path):
                folder_files.append(file_name)
        
        folder_dict[folder_name] = folder_files

# Save the dictionary to a JSON file
json_file_path = 'parent_child.json'  # Path to save the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(folder_dict, json_file, indent=4)

print("JSON file created successfully!")
