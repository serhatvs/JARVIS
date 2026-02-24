import requests
import os

MODEL_URL = "https://huggingface.co/TheBloke/Llama-3-8B-GGUF/resolve/main/llama-3-8b.Q4_K_M.gguf"
MODEL_PATH = os.path.join("models", "llama-3-8b.Q4_K_M.gguf")

if not os.path.exists("models"):
    os.makedirs("models")

print(f"Downloading Llama 3 model from {MODEL_URL} ...")
response = requests.get(MODEL_URL, stream=True)
with open(MODEL_PATH, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
print(f"Model downloaded to {MODEL_PATH}")
