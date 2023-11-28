import json

# Load the JSON file containing a list of dictionaries
with open('label_mapping.json', 'r') as file:
    data = json.load(file)

# Merge dictionaries from the list into a single dictionary
merged_dict = {}
for item in data:
    merged_dict.update(item)

# Save the merged dictionary as a new JSON file
with open('new_mapping.json', 'w') as outfile:
    json.dump(merged_dict, outfile, indent=4)  # Save with indentation for readability


print("DONE!!!!")