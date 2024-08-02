import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3
from unittest import result
from time import strftime
from ast import main
from tkinter import *
import tkinter as tk
import os
import sys
from PIL import Image, ImageTk


root = Tk()

root.title("Virtual Desktop Assistant")

root.geometry("524x370")


# def vda():
# os.system('VDAF.py')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# # to select voice


def vda():
    def speak(audio):
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!!")
        elif hour >= 12 and hour <= 18:
            speak("Good Afternoon!! ")
        else:
            speak("Good Evening!!")

        speak("How can I help you?")

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone()as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said:", query)

        except Exception as e:
            print("Say that again please...")
            speak("Say that again please...")
            return "None"
        return query

    if __name__ == "__main__":
        wishMe()
        while True:
            if 1:
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    speak("Searching wikipedia...")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                elif 'the time' in query:
                    strtime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir the time is {strtime}")
                elif 'open google' in query:
                    webbrowser.open("google.com")


# GUI CODE
root.iconbitmap(
    ("C:\\Users\Suraj\\OneDrive\\Desktop\\py\\GUI5.ico"))

img = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Suraj\\OneDrive\\Desktop\\py\\VDA7.jpg"))


imagepanel = Label(root, image=img)
imagepanel.pack(side='bottom', fill='both')

root.configure(bg="#00FFFF")

root.resizable(False, False)


F1 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)

F1.pack(side=BOTTOM, fill="x")

F2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
F2.pack(side=BOTTOM, fill="x")


l = Button(F1, text="Start Now", command=vda)
l.pack(pady=15)


l = Button(F1, text="Stop", command=root.destroy)
l.pack(pady=15)

root.mainloop()
