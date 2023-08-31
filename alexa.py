import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

import os 

# import tkinter as tk
# from tkinter import ttk
# from tkinter import *




# root = Tk()  # create root window
# root.title("image2OMR ver:1.0 - Image to OMR reader")
# root.config(bg="gray")
# # root.geometry("1360x768+0+0")
# root.geometry("800x600")
# # frame1 = Frame(root, width=600, height=400)
# frame1.place(x=100,y=110)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# root.mainloop()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            # lbl=Label(root,text="listening.....", fg="blue").place(x=100,y=100)
            # header=Label(root,text="Listening.......", padx=100, fg="lightgray", font=("Arial-wide",14, "bold")).place(x=100,y=100)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Computer' in command:
                command = command.replace('Computer', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    # elif 'date' in command:
    #     talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'shut down' in command:
        sec=5
        talk(f"Computer is shutting down within {sec} seconds")
        os.system(f"shutdown /s /t {sec}") 
    else:
        talk('Please say the command again.')


while True:
    run_alexa()

    