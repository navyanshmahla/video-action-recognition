import os
import pandas as pd

# Path to your test data folder
folder_path = './test_data'

# Fetch all file paths in the directory
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_paths.append(os.path.join(root, file))


a = 1

# Create a DataFrame with file paths and NA values
df = pd.DataFrame({'path': file_paths, 'label': a * len(file_paths)})


# Save DataFrame to a CSV file
df.to_csv('test.csv', index=False)
print("DONE!!")