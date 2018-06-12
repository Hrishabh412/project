#!/usr/bin/env python3


#IMPORT LIBRARIES
import speech_recognition as sr
import os


#RECOGNIZER DEFINED
r=sr.Recognizer()


	## CREATING FUNCTIONS ##

#ASKS FOR THE FILE/FOLDER NAME IF REQUIRED
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



#ASKS FOR THE LOCATION IF REQUIRED 
def ask_path():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the path or location ?")
		os.system("espeak -v female3 'can you please tell me the location of folder'")
		audio=r.listen(source)
	try:
		raw_path=r.recognize_google(audio)
		strip_data=raw_path.strip()
		split_data=strip_data.split()
		print(split_data)
	
		## THINK FOR THE SOLUTION ##

	except:
		print("Sorry, could Not Understand!!")
		os.system("espeak -v female3 'sorry could not understand'")
		pass



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


 	## MAIN PART #


#INITIAL INTRACTION WITH USER
with sr.Microphone() as  source:
	r.adjust_for_ambient_noise(source)
	print ("Heyyy, Whatsup chief!!!")
	os.system("espeak -v female3 'Hello Sir'")
	print("How can i help you?")
	os.system("espeak -v female3 'How can i help you'")	
	audio=r.listen(source)

try:
	
	sppeak=r.recognize_google(audio)	#speech_ip --> VOICE INPUT
	print(speak)
	
	#VOICE DATA CLEANING
	stripped_data=speak.strip()		#____Removing extra spaces
	data=stripped_data.split()		#____Fetching individual words spoken
	print(data)
	
	if data=='make' or 'create' or 'mk':
		create_dir()
	elif data=='delete' or 'remove' or 'drop' or 'rm':
		remove_dir()
	elif data=="rename" :
		rename_dir()
	else:
		print("sorry")
	

except:
	print("Could Not Understand!!")
	
