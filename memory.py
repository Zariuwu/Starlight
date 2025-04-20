import json

# Load short-term memory (from short_term.json)
def load_memory(memory_type="short_term", file_path=None):
    if memory_type == "short_term":
        file_path = file_path or "short_term.json"
    elif memory_type == "long_term":
        file_path = file_path or "long_term.json"
    else:
        print("Invalid memory type.")
        return {}

    try:
        with open(file_path, "r") as file:
            memory_data = json.load(file)
            print(f"{memory_type.capitalize()} memory loaded successfully!")
            return memory_data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return {}  # Return empty dict if the file doesn't exist
    except json.JSONDecodeError:
        print(f"Error: Failed to decode {file_path}.")
        return {}  # Return empty dict if there's an error reading the file

# Save short-term/long-term memory (to short_term.json/long_term.json)
def save_memory(memory_data, memory_type="short_term", file_path=None):
    if memory_type == "short_term":
        file_path = file_path or "short_term.json"
    elif memory_type == "long_term":
        file_path = file_path
