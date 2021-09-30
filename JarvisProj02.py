import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
#use this to select a random intro
import random
#going to use this to open the internet browser or other programs
from pynput import mouse
import python_weather
import asyncio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
hour = int(datetime.datetime.now().strftime('%I'))
currenttemp = 00

#A list of things Bobby Joe says when he is started
RobotGreetings=['The fuck you want now?','Hey there','What can I do for you?','Whoah oh, bobby joe','another question for the brain wiz!', 'Robo-nose activated', 'Happy New Year']
RobotThanks=['You bet','of course','any time dingle fuss','the brain wiz helps all','no problem']


def talk(text):
    engine.say(text)
    engine.runAndWait()

#Have the bot say hello when starting up
engine.say(random.choice(RobotGreetings))

#Weather Setup
async def getweather():
    print("--Get Weather Activated--")
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)
    # fetch a weather forecast from a city
    weather = await client.find("Farmingdale")
    #say the temperature
    print((weather.current.temperature), 'degrees')
    global currenttemp
    currenttemp=(str(weather.current.temperature))
    #talk('the current temperature is')
    #talk(str(weather.current.temperature))
    #talk('degrees')
    
    await client.close()
    return

def take_command():
    try:
        with sr.Microphone() as source:
            #if talk once = 1 then dont say hi again
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bobby joe' in command:
                print("You said", command)
                command = command.replace('bobby joe', '')
                
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
        #Tell The Time
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('the current time is ' + time)
        if hour<=6:
            talk("wow late night bitch?")
        else:
            talk("Hope your day has been good")

        #Wikipedia Person Lookup
    elif 'who exactly is' in command:
        person = command.replace('who exactly is', '')
        engine.say('Hmmm. lets see')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

        #Weather-Temperature
    elif 'weather' in command:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())
        talk('the current temperature is')
        talk(currenttemp)
        talk('degrees')
    elif 'temperature' in command:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())
        talk('the current temperature is')
        talk(currenttemp)
        talk('degrees')

        #Timer-currently gets mixed up with time
    elif 'timer' in command:
        print("Timer")

    elif 'thanks' in command:
        #Have the bot say hello when starting up
        talk(random.choice(RobotThanks))

        #Error-Didnt Hear
    else:
        talk('Im sorry what')
'''
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
'''
while True:
    run_alexa()
