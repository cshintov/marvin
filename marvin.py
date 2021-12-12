""" Module Marvin """

import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser

import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 145)
engine.setProperty('voice', voices[16].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speack('Good morning, Sir!')
    elif hour >= 12 and hour < 18:
        speack('Good afternoon, Sir!')
    else:
        speak('Good evening, Sir!')

    speak('What can I do for you?')

def take_command():
    """ Listens for commands from user """

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        command = r.recognize_google(audio, language='en-in')
        print('User said: ', command)

    except Exception as err:
        print(err)
        print("Sorry, can you say that again please?")
        return "None"

    return command

def search_wikipedia(command):
    speak('Searching Wikipedia...')
    command = command.replace('wikipedia', '')
    results = wikipedia.summary(command, sentences=3)
    speak('According to Wikipedia')
    print(results)
    speak(results)

if __name__ == '__main__':
    wish_me()

    while True:
        command = take_command().lower()

        if 'wikipedia' in command:
            search_wikipedia(command)

        elif 'open youtube' in command:
            webbrowser.open('youtube.com')

        elif 'the time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            speak(f'Sir, the time is ${time}')
