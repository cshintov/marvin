""" Utility functions """

import re
import sys
import time
import threading
import pyttsx3
from tqdm import tqdm

class Speaker:
    def __init__(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 145)
        engine.setProperty('voice', voices[16].id)
        self.engine = engine

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

def wait(duration, alert_string):
    """ Duration in seconds """
    speaker = Speaker()
    for _ in tqdm(
            range(duration), 
            desc="waiting...", 
            ascii=True,
            file=sys.stdout):
        time.sleep(1)
    speaker.speak(alert_string)

def set_alarm(duration, alert_string="What should I say?"):
    t1 = threading.Thread(target=wait, args=(duration, alert_string))
    t1.start()

def convert_to_seconds(duration):
    duration += ' '
    cur, unit = '', ''
    hr, mn, sc = 0, 0, 0

    for char in duration:
        if char.isdigit():
            cur += char
        elif char.isalpha():
            unit += char
        elif char == ' ':
            if 'hour' in unit:
                hr = int(cur)
                cur = unit = ''
            elif 'minute' in unit:
                mn = int(cur)
                cur = unit = ''
            elif 'second' in unit:
                sc = int(cur)
                cur = unit = ''

    return hr * 3600 + mn * 60 + sc


assert convert_to_seconds('1 hour 30 minutes 40 seconds') == 1 * 3600 + 30 * 60 + 40
assert convert_to_seconds('1 hour 30 minutes') == 1 * 3600 + 30 * 60
assert convert_to_seconds('30 minutes') == 30 * 60
assert convert_to_seconds('30 seconds') == 30
