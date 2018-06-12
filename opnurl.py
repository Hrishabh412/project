#!/usr/bin/python3

import speech_recognition as sr
import webbrowser as wb

firefox_path = '/usr/bin/firefox %s'

r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("say any url")
	audio=r.listen(source)

try:
	text=r.recognize_google(audio)
	print("you said" + text)
	wb.get(firefox_path).open(text)	
except Exception as e:
	print(e)
