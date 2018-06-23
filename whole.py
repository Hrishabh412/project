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

#CREATING FOLDER
def create_dir():
	dir_name=ask_name()
	os.system('mkdir '+dir_name)

#REMOVING FOLDER
def remove_dir():
	dir_name=ask_name()
	os.system('rmdir '+dir_name)
	
#RENAMING FOLDER
def rename_dir():
	source_dir=ask_name()
	new_dir=ask_name()
	os.system('mv '+source_dir+' '+new_dir)

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
       #file handling

	if "file handling" in final_txt:
		
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			os.system("espeak -v female3 'which operation want to perform'")
			print("say somthing")
			audio=r.listen(source)
			print("done")

		try:
			text=r.recognize_google(audio)
			print("you said" +text)
			strip_txt=text.strip()
			final_text=strip_txt.split()
			print(final_text)
       #file handling


			if final_text=='make' or "create" or "build":
				create_file()

			elif final_text=="delete" or "remove" or 'rm':
				remove_file()
			else:
				print("sorry")
		except Exception as e:
			print (e)
	
	#directory handling

	elif "directory handling" in final_txt:
		
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			os.system("espeak -v female3 'which operation want to perform on directory'")
			print("say somthing")
			audio=r.listen(source)
			print("done")

#
		try:
			text1=r.recognize_google(audio)
			print("you said" +text1)
			strip_txt=text1.strip()
			final_text1=strip_txt.split()
			print(final_text1)	

			
			if final_text1=='make' or "create" or "build":
				create_dir()

			elif final_text1=="delete" or "remove" or 'rm':
				remove_dir()

			else:
				rename_dir()
		except Exception as e:
			print (e)
	

	elif 'install' or 'download' in final_txt:

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
		
		print("Sorry, could Not Understand!!")
		os.system("espeak -v female3 'sorry could not understand'")
		pass	
except Exception as e:
	print (e)






