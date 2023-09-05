import json
import sys

# Replace 'your_file.json' with the path to your JSON file
with open('schema.json', 'r') as json_file:
    data = json.load(json_file)

columns = []
for column_name, column_data in data['properties'].items():
    column_type = column_data['type']
    columns.append((column_name, column_type))

# Convert columns to a JSON string
columns_json = json.dumps(columns)

# Print the JSON string
print(columns_json)

# You can also pass this JSON string as a command-line argument to another program
# Example: python program2.py "{your_json_string_here}"
