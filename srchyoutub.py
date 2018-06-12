#!/usr/bin/python3

import speech_recognition as sr
import webbrowser as wb

#obtain audio from microphone
url='https://www.youtube.com/results?search_query='
r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("say song name")
	audio=r.listen(source)

#recognizing the speech
try:
	text=r.recognize_google(audio)
	print("you said " +text)
	wb.open_new(url+text)
except Exception as e:
	print (e)


