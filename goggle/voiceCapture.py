import speech_recognition as sr
import cv2, time
import random
import pyttsx3

# Function to recogonize particular word
def voiceRec():
	r = sr.Recognizer()
	# word required to recogonize
	keyWord = 'image'

	with sr.Microphone() as source:
		print('Please start speaking..\n')
		while True: 
			audio = r.listen(source)
			try:
				text = r.recognize_google(audio)
				if keyWord.lower() in text.lower():
					response_voice()
					print ('conveted text from audio',text)
					capture()
			except Exception as e:
				print('Please speak again.')

def capture():
	#creating a video object
	video = cv2.VideoCapture(0) 
	#Variable
	a = 0

	while True:
		a = a + 1
		cv2.imshow("Capturing",frame)

		break
	showPic = cv2.imwrite(str(random.randint(1100,111110)) + ".jpg", frame)
	print(a)
	# shutdown the camera
	video.release()

	cv2.destroyAllWindows 
	return 0


def response_voice():
	engine = pyttsx3.init()
	engine.say("Image Captured")
	engine.runAndWait()
	return 0
# exectution starts here
voiceRec()