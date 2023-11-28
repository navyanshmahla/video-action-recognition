# import os
# import pandas as pd

# # Directory containing video folders labeled by their class
# base_directory = "./data"

# video_files = []

# # Iterate through each folder (assuming each folder is a label)
# for label in os.listdir(base_directory):
#     label_dir = os.path.join(base_directory, label)
    
#     # Check if it's a directory
#     if os.path.isdir(label_dir):
#         # Iterate through video files in the folder
#         for video_file in os.listdir(label_dir):
#             video_path = os.path.join(label_dir, video_file)
#             # Append video path and label to the list
#             video_files.append([video_path, idx])

# # Create a DataFrame from the list of video files
# df = pd.DataFrame(video_files)

# # Save DataFrame to a CSV file without column names
# df.to_csv('train.csv', index=False, header=False)

# print("DONE!!")

import os
import pandas as pd
import json 

# Directory containing video folders labeled by their class
base_directory = "./val_data"

video_files = []
label_map = {}  # Dictionary to map labels to integers
label_index = 0  # Initial index for labels

# Iterate through each folder (assuming each folder is a label)
for label in os.listdir(base_directory):
    label_dir = os.path.join(base_directory, label)
    
    # Check if it's a directory
    if os.path.isdir(label_dir):
        # Assign an index to the label and store in the label_map dictionary
        label_map[label] = label_index
        label_index += 1
        
        # Iterate through video files in the folder
        for video_file in os.listdir(label_dir):
            video_path = os.path.join(label_dir, video_file)
            # Append video path and label index to the list
            video_files.append([video_path, label_map[label]])

# Create a DataFrame from the list of video files
df = pd.DataFrame(video_files)

# Save DataFrame to a CSV file without column names
df.to_csv('val.csv', index=False, header=False)
print(label_map.items())
label_df = pd.DataFrame(list(label_map.items()), columns=['Label', 'Index'])

# Save DataFrame to a JSON file without square brackets
# with open('label_mapping.json', 'w') as json_file:
#     for record in label_df.to_dict(orient='records'):
#         json.dump(record, json_file)
#         json_file.write('\n')  # Add a newline to separate records

# Save DataFrame to a CSV file
label_df.to_csv('label_mapping.csv', index=False)

# Read the CSV file and convert it to a JSON file
df_from_csv = pd.read_csv('label_mapping.csv')
df_from_csv.to_json('label_mapping.json', orient='records')

label_df.to_json('label_mapping.json', orient='records')

label_dict = label_df.set_index('Label').to_dict()['Index']
with open('label_mapping.json', 'w') as json_file:
    json.dump(label_dict, json_file)


print("DONE!!")