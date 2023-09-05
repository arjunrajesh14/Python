import sys
import json

# Check if an argument is provided
if len(sys.argv) != 2:
    print("Usage: program2.py <columns_json>")
    sys.exit(1)

# Get the JSON string argument
columns_json = sys.argv[1]

# Parse the JSON string back into a Python list
columns = json.loads(columns_json)

print(columns)

# Now you can use the 'columns' list in program2 for data generation or other tasks
