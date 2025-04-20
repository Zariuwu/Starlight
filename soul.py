import json

# Load the soul (from Soul.json)
def load_soul(file_path="Soul.json"):
    try:
        with open(file_path, "r") as file:
            soul_data = json.load(file)
            print("Soul loaded successfully!")
            return soul_data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return {"version": 1, "data": {}}  # Return default structure if file doesn't exist
    except json.JSONDecodeError:
        print("Error: Failed to decode Soul.json.")
        return {"version": 1, "data": {}}  # Return default if there is an issue reading the file

# Save the soul (to Soul.json)
def save_soul(soul_data, file_path="Soul.json"):
    try:
        with open(file_path, "w") as file:
            json.dump(soul_data, file, indent=4)
            print("Soul saved successfully!")
    except Exception as e:
        print(f"Error saving Soul: {e}")
