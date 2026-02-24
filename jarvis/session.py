
class SessionMemory:
	"""Oturum (session) hafızası yönetimi."""
	def __init__(self):
		self._memory = []

	def add(self, item):
		"""Oturum hafızasına yeni bir öğe ekle."""
		self._memory.append(item)

	def get_all(self):
		"""Tüm oturum hafızasını döndür."""
		return list(self._memory)

	def get_last(self, n=1):
		"""Son n öğeyi döndür."""
		return self._memory[-n:] if n > 0 else []

	def clear(self):
		"""Oturum hafızasını sıfırla."""
		self._memory.clear()

	def __len__(self):
		return len(self._memory)
