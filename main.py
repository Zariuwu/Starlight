# filepath: c:\Users\ZariS\Documents\Starlight Project\Starlight\src\main.py
import json
from flask import Flask
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Load the AI model
model_name = "llama3"  # Replace with the actual model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load state from Soul.json
def load_state(file_path="data/Soul.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save state to Soul.json
def save_state(state, file_path="data/Soul.json"):
    with open(file_path, "w") as file:
        json.dump(state, file)

# Example route for Flask
@app.route("/")
def home():
    return "Welcome to Starlight!"

if __name__ == "__main__":
    app.run(debug=True)