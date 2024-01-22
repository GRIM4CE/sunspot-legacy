import json

# Read the current number from the JSON file
def incrementJSONFileNumber(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            current_number = data.get('number', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle the case where the file doesn't exist or is not valid JSON
        current_number = 0

    # Increase the number by 1
    new_number = current_number + 1

    # Write the updated number back to the JSON file
    with open(file_path, 'w') as file:
        json.dump({'number': new_number}, file)
