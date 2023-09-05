import json

# Load the JSON schema from a file
with open('schema.json', 'r') as schema_file:
    schema = json.load(schema_file)

# Extract the properties section from the schema
properties = schema.get('properties', {})

columns = []
for column_name, column_data in properties.items():
    column_type = column_data['type']
    columns.append((column_name, column_type))
for column_name, column_type in columns:
    print(f"Column Name: {column_name}, Type: {column_type}")

