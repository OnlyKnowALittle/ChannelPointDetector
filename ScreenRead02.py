#gui - locate portions of screen
import pyautogui
#import image ability
from PIL import Image
import pytesseract
#Following three lines allow for searching of both monitors
from PIL import ImageGrab
from functools import partial
import re
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
#used to detect start key
import keyboard
#used for voice
import pyttsx3

#Getting the voice section setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 250)
engine.setProperty('volume', 1.0)
engine.say('Loaded and ready to read')

#this function is used to get pyttsx3 to actually talk - putting engine.say alone will not allow speech to work
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

ScreenGrab = (r'C:/Users/billt/Documents/Python/images/Screen_Read/NVScreen.png')
ScreenTest = (r'C:/Users/billt/Documents/Python/images/Screen_Read/screen.png')

#take screenshot of a region
def take_screenshot():
    myScreenshot = pyautogui.screenshot(region=(530,332,900,601))
    myScreenshot.save(ScreenGrab)

#read text from screenshot and then read
def read_screenshot():
    value = Image.open(ScreenGrab)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(value, config=custom_config)
    print(text)
    #read out loud
    speak(text)
    __init__()

def __init__():
    print('waiting for f9 bro')
    keyboard.wait('F9')
    print('okay!')
    take_screenshot()
    read_screenshot()

__init__()