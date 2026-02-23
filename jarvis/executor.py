
class Executor:
	"""Risk-aware görev yürütücüsü."""
	def __init__(self):
		pass

	def execute(self, task, risk_score):
		"""Görevi risk puanına göre yürütür.
		0–30: otomatik
		30–70: kullanıcı onayı
		70+: engellenir
		"""
		if risk_score <= 30:
			print(f"Otomatik yürütülüyor: {task}")
		elif risk_score <= 70:
			print(f"Onay gerekli: {task}")
		else:
			print(f"Yüksek risk: {task} engellendi!")
