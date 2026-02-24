"""
reflection.py
JARVIS: Reflection ve öğrenme hookları
"""

from typing import Any, Dict, Callable, List, Optional
import datetime

class Reflection:
    """
    Reflection mekanizması: Ajanın geçmiş deneyimlerinden ders çıkarması ve kendini geliştirmesi için temel yapı.
    """
    def __init__(self):
        self.reflection_log: List[Dict[str, Any]] = []
        self.hooks: List[Callable[[Dict[str, Any]], None]] = []

    def add_hook(self, hook: Callable[[Dict[str, Any]], None]) -> None:
        """Reflection sonrası çalışacak bir öğrenme hook'u ekler."""
        self.hooks.append(hook)

    def reflect(self, event: Dict[str, Any]) -> None:
        """
        Bir olay veya deneyim üzerinde reflection yapar, loglar ve hook'ları tetikler.
        Args:
            event: {'type': str, 'result': Any, 'timestamp': datetime, ...}
        """
        event['timestamp'] = datetime.datetime.now()
        self.reflection_log.append(event)
        for hook in self.hooks:
            hook(event)

    def get_reflections(self, event_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Reflection geçmişini döndürür. İstenirse sadece belirli bir event_type için filtreler.
        """
        if event_type:
            return [e for e in self.reflection_log if e.get('type') == event_type]
        return self.reflection_log

# Örnek öğrenme hook'u

def simple_learning_hook(event: Dict[str, Any]):
    if event.get('type') == 'task_result':
        # Burada basit bir öğrenme işlemi yapılabilir
        print(f"Öğrenme Hook'u: Görev sonucu kaydedildi: {event.get('result')}")

# Kullanım örneği
# reflection = Reflection()
# reflection.add_hook(simple_learning_hook)
# reflection.reflect({'type': 'task_result', 'result': 'Başarılı'})
