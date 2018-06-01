#!/usr/bin/python3

import speech_recognition as sr
import os
import sys
import time

r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("say any command")
	audio=r.listen(source)


try:
	text=r.recognize_google(audio)
	print("you said " +text)
	a=os.system(r.recognize_google(audio))
	print(a)
		
except Exception as e:
	print (e)
