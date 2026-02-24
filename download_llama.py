# Llama model dosyasını indirmek için örnek script
# Not: Büyük dosya (~4GB+) gerektirir. Aşağıdaki URL örnektir, kendi modelinizi seçebilirsiniz.
import requests
import os

def download_llama_model(url, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename

if __name__ == "__main__":
    # Örnek: HuggingFace veya başka bir kaynaktan GGUF formatında model URL'si girilmeli
    MODEL_URL = "https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf"
    DEST = "models"
    print("İndirme başlatılıyor...")
    path = download_llama_model(MODEL_URL, DEST)
    print(f"Model indirildi: {path}")
