#!/usr/bin/python3

import speech_recognition as sr
import os

r=sr.Recognizer()

#creating functions
def ask_name():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the name?")
		os.system("espeak -v female3 'can you please tell me the name of folder'")
		audio=r.listen(source)
	try:
		name=r.recognize_google(audio)
		return name
	except:
		print("Sorry, could Not Understand!!")
		os.system("espeak -v female3 'Sorry could not understand'")
		pass


#CREATING File
def create_file():
	file_name=ask_name()
	os.system('touch '+file_name)

#REMOVING File
def remove_file():
	file_name=ask_name()
	os.system('rm '+file_name)

#main part

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	os.system("espeak -v female3 'Hello Sir'")
	os.system("espeak -v female3 'How can i help you'")
	print("say somthing")
	audio=r.listen(source)
	print("done")

#voice clearing
try:
	text=r.recognize_google(audio)
	print("you said" +text)
	strip_txt=text.strip()
	final_txt=strip_txt.split()
	print(final_txt)

	if final_txt=='make' or "create" or "build":
		create_file()
	elif final_txt=="delete" or "remove" or 'rm':
		remove_file()
	
	else:
		
		print("Sorry, could Not Understand!!")
		os.system("espeak -v female3 'sorry could not understand'")
		pass	
except Exception as e:
	print (e)
