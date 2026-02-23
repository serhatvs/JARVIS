from jarvis.agents import *
from jarvis.planner import *
from jarvis.executor import *
from jarvis.session import *
from jarvis.reflection import *
from jarvis.voice import *



def main():
    print("JARVIS başlatılıyor...")

    # Basit test senaryosu
    # Görev ağacı oluştur
    root = Task("Ana Görev")
    sub1 = Task("Alt Görev 1")
    sub2 = Task("Alt Görev 2")
    root.add_subtask(sub1)
    root.add_subtask(sub2)
    tree = TaskTree(root)

    print("Görev Ağacı:")
    tree.traverse()

    # Risk-aware executor ile görev yürütme
    executor = Executor()
    executor.execute("Alt Görev 1", risk_score=20)
    executor.execute("Alt Görev 2", risk_score=50)
    executor.execute("Ana Görev", risk_score=80)


if __name__ == "__main__":
    main()
