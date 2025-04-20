import json
import requests
import configparser

# load brain config
with open("config.json", "r") as f:
    config = json.load(f)

# base Brain class
class Brain:
    def chat(self, prompt, history=[]):
        raise NotImplementedError("chat not implemented")

# OLLAMA BRAIN
class OllamaBrain(Brain):
    def __init__(self):
        self.api = config["ollama"]["api_base"]
        self.model = config["ollama"]["model"]

    def chat(self, prompt, history=[]):
        messages = [{"role": "system", "content": "You are Starlight, an evolving AI guide."}]
        for h in history:
            messages.append({"role": "user", "content": h["user"]})
            messages.append({"role": "assistant", "content": h["ai"]})
        messages.append({"role": "user", "content": prompt})

        res = requests.post(
            f"{self.api}/chat/completions",
            json={"model": self.model, "messages": messages}
        )
        return res.json()["choices"][0]["message"]["content"]

# DEEPSEEK BRAIN (placeholder - you’ll connect real model later)
class DeepseekBrain(Brain):
    def __init__(self):
        self.path = config["deepseek"]["path"]

    def chat(self, prompt, history=[]):
        return "🧠 DeepSeek is not wired yet. (stub response)"

# brain selector
def get_brain():
    brain_type = config["brain"]
    if brain_type == "ollama":
        return OllamaBrain()
    elif brain_type == "deepseek":
        return DeepseekBrain()
    else:
        raise ValueError("Unknown brain in config.json")
