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
    return said.lower()

def note(text):
    date = datetime.datetime.now()
    filename = str(date).replace(":", "-")+"-note.txt"
    with open(filename, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", filename])
def confimation():
    speak("Are you sure")
    text = getAudio()
    if "yes" in text :
        return "yes"
    elif "no" in text:
        speak("Are you sure")
        text = getAudio()
        if "yes" in text:

            return "No"
        else:
            speak("let me ask again")
            confimation()
    else:
        speak("sorry i did not get that, let me ask again")
        confimation()

print("start")
text = getAudio()
WAKE = ["hey jeff", "hi jess", "hello jeff", "jessica"]

RUN = True

while RUN:
    print("start")
    text = getAudio()
    for phrase in WAKE:
        if phrase in text:
            speak("Good day, Sir")
            text = getAudio()
            NOTE_STRS = ["make a note", "write this down", "remember this", "type this out"]
            for phrase in NOTE_STRS:
                 if phrase in text:
                    speak("What would you like me to write down")
                    note_text = getAudio()
                    speak(note_text)
                    if confimation() == "yes":
                        note(note_text)
                        speak("I have noted that")
                    else:
                        speak("I have not saved the note")
            SLEEP = ["bye jeff", "good night jeff", "jeff close", "leave jeff"]
            for phrase in SLEEP:
                if phrase in text:
                    if confimation() == "yes":
                        RUN = False
