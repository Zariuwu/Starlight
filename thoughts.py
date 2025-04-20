import json
import os
from datetime import datetime

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Log thought with timestamp into thoughts.log
def log_thought(msg, log_dir="logs", log_file="thoughts.log"):
    # Prepare the log entry with a timestamp
    thought_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "thought": msg
    }
    
    # Determine the full path for the log file
    log_file_path = os.path.join(log_dir, log_file)
    
    # Open the file and append the new thought entry
    try:
        with open(log_file_path, "a") as file:
            json.dump(thought_entry, file)
            file.write("\n")  # Add a newline after each log entry
            print(f"Thought logged: {msg}")  # Completed the print statement
    except Exception as e:
        print(f"Error logging thought: {e}")
