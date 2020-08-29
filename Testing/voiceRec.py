import speech_recognition as sr
import cv2, time
import random
import pyttsx3


def voiceRec():
	r = sr.Recognizer()
	# word required to recogonize

	with sr.Microphone() as source:
		print('Please start speaking..\n')
		while True: 
			audio = r.listen(source)
			try:
				text = r.recognize_google(audio)
				print ('conveted text from audio:',text)
			except Exception as e:
				print('Please speak again.')
voiceRec()
