
class Task:
	"""Bir görevi temsil eden temel sınıf."""
	def __init__(self, name, subtasks=None):
		self.name = name
		self.subtasks = subtasks if subtasks else []

	def add_subtask(self, task):
		self.subtasks.append(task)

	def __repr__(self):
		return f"Task(name={self.name}, subtasks={len(self.subtasks)})"


class TaskTree:
	"""Görevlerin hiyerarşik olarak tutulduğu ağaç yapısı."""
	def __init__(self, root_task):
		self.root = root_task

	def traverse(self):
		def _traverse(task, depth=0):
			print("  " * depth + f"- {task.name}")
			for sub in task.subtasks:
				_traverse(sub, depth+1)
		_traverse(self.root)
