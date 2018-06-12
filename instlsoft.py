#!/usr/bin/python3

import speech_recognition as sr
import os

r=sr.Recognizer()


with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("say any command")
	audio=r.listen(source)
	print("done")

try:
	text=r.recognize_google(audio)
	print("you said " +text)
	strip_txt=text.strip()
	final_txt=strip_txt.split()
	print(final_txt)
	if 'install' or 'download' in final_txt:

		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print("say what you want to install")
			audio=r.listen(source)
			print("done")

		try:
			text=r.recognize_google(audio)
			print("you said " +text)
			print(text) 
			a=os.system("sudo apt install  "+text)
			print(a)

	
		
		except Exception as e:
			print (e)
	else:
		print("sorry")
except Exception as e:
	print(e)
