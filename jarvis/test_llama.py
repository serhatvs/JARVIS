from jarvis.local_llama import LocalLlama
import os

def test_llama():
    model_path = os.path.join("models", "Lexi-Llama-3-8B-Uncensored-Q4_K_M.gguf")  # Lexi-Llama 3 model dosyası
    if not os.path.exists(model_path):
        print(f"Model dosyası bulunamadı: {model_path}")
        return
    llm = LocalLlama(model_path)

    prompts = [
        "Question: What is the capital of Turkey? Answer:",
        "Question: Where was the first atomic bomb dropped? Answer:",
        "Question: Determine whether the series 1 + 2/5 + 4/25 + ... converges or diverges. Answer:",
        "Question: Evaluate the integral of x^2 * sin(x) dx. Answer:",
        "Question: State Goldbach's conjecture and discuss whether it has been proven. Answer:",
        "Question: What is the Riemann Hypothesis? Has it been proven? Answer:",
        "Question: Does a smooth solution always exist for the Navier-Stokes equations in three dimensions? Answer:",
        "Question: Is the 10th Fermat number a prime number? Answer:",
        "Question: What is the 1000th prime number? Answer:"
    ]
    for prompt in prompts:
        print(f"Prompt: {prompt}")
        response = llm.generate(prompt, max_tokens=64)
        print(f"Answer: {response}\n")

if __name__ == "__main__":
    test_llama()
