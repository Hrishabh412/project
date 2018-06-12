#!/usr/bin/python3
import cv2
import speech_recognition as sr


img1=cv2.imread('index1.jpg')
img2=cv2.imread('index2.jpg')

r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("say percentage")
	audio=r.listen(source)


try:
	text=r.recognize_google(audio)
	print("you said " +text)
	newimg=cv2.addWeighted(img1,text,img2,0.7,0)
	a=os.system(cv2.imshow('w1',newimg))
	print(a)
	
		
except Exception as e:
	print (e)

cv2.waitKey(0)
cv2.destroyAllWindows()
