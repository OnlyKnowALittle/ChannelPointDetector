import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hey there')
engine.say('Bobby Joe here!')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('Bobb Joe 1.0 - Listening Mode...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'bobby joe' in command:
            print(command)
except:
    pass