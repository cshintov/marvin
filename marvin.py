""" Module Marvin """

import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

from utils import *

speaker = Speaker()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speaker.speak('Good morning, Sir!')
    elif hour >= 12 and hour < 18:
        speaker.speak('Good afternoon, Sir!')
    else:
        speaker.speak('Good evening, Sir!')

    speaker.speak('What can I do for you?')

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
    speaker.speak('Searching Wikipedia...')
    command = command.replace('wikipedia', '')
    results = wikipedia.summary(command, sentences=3)
    speaker.speak('According to Wikipedia')
    print(results)
    speaker.speak(results)

def create_alarm(command):
    duration, alert_string = command.split('and')
    set_alarm(
        int(convert_to_seconds(duration)), 
        alert_string
    )

if __name__ == '__main__':
    wish_me()

    while True:
        print('Listening...')
        command = take_command().lower()

        if 'stop listening' in command:
            input()

        if 'wikipedia' in command:
            search_wikipedia(command)

        elif 'open twitter' in command:
            webbrowser.open('twitter.com')

        elif 'open google' in command:
            webbrowser.open('google.com')

        elif 'the time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            speaker.speak(f'Sir, the time is {time}')

        elif 'set alarm' in command:
            try:
                create_alarm(command.replace('set alarm for', ''))
            except ValueError:
                continue
