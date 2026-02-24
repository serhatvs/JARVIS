from jarvis.executor import Executor

def test_executor():
    executor = Executor()
    print('--- Düşük risk (otomatik) ---')
    executor.execute('Dosya sil', 20)
    print('--- Orta risk (onay gerekli) ---')
    executor.execute('Sistem ayarlarını değiştir', 50)
    print('--- Yüksek risk (engellenir) ---')
    executor.execute('Kritik sistem dosyasını sil', 90)

if __name__ == "__main__":
    test_executor()
