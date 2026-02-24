# Llama modelini local olarak çalıştırmak için temel arayüz
# (örnek: llama-cpp-python)

from typing import List

try:
    from llama_cpp import Llama
except ImportError:
    Llama = None

class LocalLlama:
    def __init__(self, model_path: str):
        if Llama is None:
            raise ImportError("llama-cpp-python yüklü değil. Lütfen requirements.txt dosyasına ekleyin ve yükleyin.")
        self.llama = Llama(model_path=model_path)

    def generate(self, prompt: str, max_tokens: int = 128) -> str:
        output = self.llama(prompt, max_tokens=max_tokens)
        return output["choices"][0]["text"].strip()
