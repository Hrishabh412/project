#!/usr/bin/python3

import speech_recognition as sr
import os

r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("say somthing" )
	audio=r.listen(source)
	print("done")

try:
	text=r.recognize_google(audio)
	print("you said" +text)
	strip_text=text.strip()
	final_text=strip_text.split()
	print (final_text)

	if "open" or "on" in final_text :
		for i in range(0,len(final_text)):
			if final_text[i]=="camera":
				a=os.system("cheese")
				print(a)
	
except Exception as e:
	print (e)
