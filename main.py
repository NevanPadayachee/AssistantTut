import os
import time
import datetime
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")
def getAudio():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio = rec.listen(source)
        said=""

        try:
            said = rec.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: "+str(e))
    return said

def note(text):
    date = datetime.datetime.now()
    filename = str(date).replace(":", "-")+"-note.txt"
    with open(filename, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", filename])

#note("nevan")

print("start")
text = getAudio()

NOTE_STRS = ["make a note", "write this down", "remember this", "type this out"]
for pharse in NOTE_STRS:
    if pharse in text:
        speak("What would you like me to write down")
        note_text = getAudio().lower()
        note(note_text)
        speak("I have noted that")
'''



if "hello" in text:
    speak("hello, how are you?")

if "what is your name" in text:
    speak("Hi I'm jess, nice to meet you")'''