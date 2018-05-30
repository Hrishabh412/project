#!/usr/bin/python3
import speech_recognition as sr

#obtain audio from microphone
r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("say something")
	audio=r.listen(source)
	
#recognizing the speech
try:
	print("you said" + r.recognize_google(audio))
	print("audio successfully recorded")
except Execption as e:
	print (e)

#write audio in wav file
with open("microphone-result.wav","wb") as f:
	f.write(audio.get_wav_data())
