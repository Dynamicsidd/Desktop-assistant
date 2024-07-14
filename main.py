

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the male voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize and return text from speech
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return ""  # Return an empty string if recognition fails
    return query

# Take command and speak it
taken_command = takecommand()
if taken_command:
    speak(taken_command)
else:
    speak("I did not understand what you said. Please try again.")

