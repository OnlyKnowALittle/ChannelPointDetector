import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
hour = int(datetime.datetime.now().strftime('%I'))

def talk(text):
    engine.say(text)
    engine.runAndWait()

RobotGreetings=['The fuck you want now?','What do you need sir?','What can I do for you?','Hey there, bobby joe is here','another question for the brain wiz!','I am cyber, I am knowledge, Im Bobby Joe']
engine.say(random.choice(RobotGreetings))

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bobby joe' in command:
                command = command.replace('bobby joe', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'bobby joe' in command:
        engine.say('Hmm lets see')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('the current time is ' + time)
        if hour>1:
            talk("wow late night bitch?")
    elif 'who exactly is' in command:
        person = command.replace('who exactly is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
