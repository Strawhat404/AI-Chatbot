import speech_recognition as sr
from gtts import gTTS
import os

recognizer = sr.Recognizer()

def listen_to_user():
    with sr.Microphone() as source:
        print("listening....")
        audio = recognizer.recognize_google(audio)
        
def speak_response(response_text):
    tts = gTTS(text=response_text,lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")