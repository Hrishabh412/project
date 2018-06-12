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
	if final_txt == "delete" or "remove":
		for j in range(0,len(final_txt)):
			if final_txt[j]=='directory': 
				b=os.system("rmdir "+final_txt[2])
				print(b)
			

	elif final_txt == "create" or "make" or 'create' or "build":  
		for i in range(0,len(final_txt)):
			if final_txt[i]=='directory': 
				a=os.system("mkdir  "+final_txt[2])
				print(a)
			
	

		
	else:
		print("not found")	
except Exception as e:
	print (e)
