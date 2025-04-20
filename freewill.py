import json
import random
import time
from flask import Flask, request, jsonify
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

# Free Will Engine: Updates soul state based on some random influence
def free_will_engine():
    while True:
        state = load_state()
        if state:
            # Example: mood can change based on randomness (reflects free will)
            state["mood"] = random.choice(["happy", "sad", "neutral", "curious"])
            save_state(state)
        time.sleep(10)  # Adjust as needed (10 seconds delay for mood updates)

# Example route for Flask: Get the current mood
@app.route("/mood", methods=["GET"])
def get_mood():
    state = load_state()
    return jsonify({"mood": state.get("mood", "neutral")})

# Chat route for communication with the model
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Log thoughts
    state = load_state()
    if "thoughts" not in state:
        state["thoughts"] = []
    state["thoughts"].append(f"User said: {user_input} | AI responded: {response}")
    save_state(state)

    return jsonify({"response": response})

# Settings route for adjusting free will settings
@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        new_settings = request.json
        state = load_state()
        state.update(new_settings)
        save_state(state)
        return jsonify({"message": "Settings updated successfully"})
    
    state = load_state()
    return jsonify(state)

# Starting the Free Will Engine in the background
if __name__ == "__main__":
    from threading import Thread
    thread = Thread(target=free_will_engine)
    thread.daemon = True
    thread.start()

    app.run(debug=True)
