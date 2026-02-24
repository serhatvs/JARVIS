# JARVIS – Just A Really Versatile Intelligent System

JARVIS, çok ajanlı, hibrit planlayıcıya sahip kişisel bir AI asistanıdır. Kod üretimi, sistem otomasyonu, risk değerlendirmesi ve sesli etkileşim gibi özelliklerle, karmaşık iş akışlarını ve projeleri kolayca yönetmenizi sağlar.

---

## Hızlı Başlangıç

```bash
git clone https://github.com/serhatvs/JARVIS.git
cd JARVIS
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python main.py
```

---

## Temel Özellikler
- Doğal dilde karmaşık hedefleri anlama ve görev ağacına dönüştürme
- Kod ve sistem otomasyonu, güvenli ve risk kontrollü yürütme
- Risk değerlendirme ve refleksiyon mekanizmaları
- Çok ajanlı işbirliği ve oturum hafızası
- Sesli etkileşim ve gerçek zamanlı geri bildirim

---

## Reflection ve Öğrenme Mekanizması

JARVIS, geçmiş görev sonuçlarından ders çıkarabilen ve kendini geliştirebilen bir reflection (öz-düşünüm) altyapısına sahiptir. `reflection.py` dosyasında, olay bazlı reflection logları tutulur ve öğrenme hook'ları ile sistemin davranışı dinamik olarak güncellenebilir.

### Kullanım Örneği

```python
from reflection import Reflection, simple_learning_hook

reflection = Reflection()
reflection.add_hook(simple_learning_hook)
reflection.reflect({'type': 'task_result', 'result': 'Başarılı'})
print(reflection.get_reflections())
```

Reflection mekanizması ile ilgili detaylar ve ileri seviye kullanım için [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md) dosyasına bakınız.

---

## Bugün Yapılanlar (24 Şubat 2026)

- Llama 2 model dosyası silindi, sistemdeki eski model kaldırıldı.
- Llama 3 (Lexi-Llama-3-8B-Uncensored-Q4_K_M.gguf) model dosyası indirildi ve entegre edildi.
- `test_llama.py` scripti Llama 3 modeline göre güncellendi ve çalıştırıldı.
- Modelin matematiksel ve bilimsel sorulara verdiği yanıtlar test edildi, sonuçlar analiz edildi.
- Zorlayıcı sorular (Goldbach hipotezi, Riemann hipotezi, Navier-Stokes, Fermat sayısı, 1000. asal sayı) ile modelin sınırları denendi.
- Llama 3'ün orchestrator olarak yeterliliği ve finetune ile performans artışı tartışıldı.
- Yerel orchestrator için alternatif açık kaynak modeller ve frameworkler önerildi.
- README güncellendi, yapılan işlemler ve teknik notlar eklendi.

---

## Katkı Sağlama
Katkılar memnuniyetle karşılanır. Lütfen PR açmadan önce kodlama ve katkı rehberini inceleyin.

---

## Dokümantasyon
- [Kapsamlı Proje Dokümantasyonu](PROJECT_DOCUMENTATION.md)
- [Günlük Kontrol Listesi](CHECKLIST.md)
- [Geliştirme Önerileri](RECOMMENDATIONS.md)

---

## Lisans
MIT License. Kişisel, akademik ve ticari kullanım için serbesttir.

---

## Güncellemeler (24.02.2026)

- Gereksiz __pycache__ klasörleri ve derlenmiş dosyalar silindi.
- Dosya düzeni sadeleştirildi.
- README ve proje dokümantasyonu güncellendi.
