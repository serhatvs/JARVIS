
# Voice-first interaction logic

import pyttsx3

def speak(text: str):
	"""
	Verilen metni sesli olarak okur.
	Basit bir TTS (Text-to-Speech) fonksiyonudur.
	"""
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()
