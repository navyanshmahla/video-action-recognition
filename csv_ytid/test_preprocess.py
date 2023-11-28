import os
import pandas as pd

import shutil

# Specify the base directory where you want to create the folders
base_directory = "./test_data"

df = pd.read_csv("./kinetics-400_test.csv")

#labels = df['label'].unique()

# Iterate over the rows of the DataFrame
# for label in labels:
#     # Get the folder name from the "FolderName" column
#     folder_name = label
#     # Create the full path for the folder
#     folder_path = os.path.join(base_directory, folder_name)
#     os.makedirs(folder_path)

folder_path_data = "./test"

for index, row in df.iterrows():
    id =row["youtube_id"]
    start = row["time_start"]
    end = row["time_end"]
    start = f"{start:06}"
    end = f"{end:06}"
    video_name = id+"_"+start+"_"+end+".mp4"
# Create the full path to the video file
    video_path = os.path.join(folder_path_data, video_name)
    print(video_name)
    print(video_path)
# Specify the destination folder
    #label = row["label"]
    #destination_folder = os.path.join(base_directory, label)
    #destination_folder = video_path
    #destination_path = os.path.join(destination_folder, video_name)
    destination_path = os.path.join(base_directory, video_name)

# Check if the source video file exists
    if os.path.exists(video_path):
        print(f"Moving {video_path} to {destination_path}")
        shutil.move(video_path, destination_path)    
    else:
        print(f"Video file not found: {video_path}")
        continue

print("DONE!!")