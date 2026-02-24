from jarvis.session import SessionMemory

def test_session_memory():
    memory = SessionMemory()
    print('--- Başlangıç ---')
    print(memory.get_all())
    memory.add('ilk komut')
    memory.add('ikinci komut')
    print('--- Ekleme sonrası ---')
    print(memory.get_all())
    print('--- Son öğe ---')
    print(memory.get_last())
    print('--- Son iki öğe ---')
    print(memory.get_last(2))
    print('--- Hafıza uzunluğu ---')
    print(len(memory))
    memory.clear()
    print('--- Temizleme sonrası ---')
    print(memory.get_all())
    print('--- Hafıza uzunluğu ---')
    print(len(memory))

if __name__ == "__main__":
    test_session_memory()
