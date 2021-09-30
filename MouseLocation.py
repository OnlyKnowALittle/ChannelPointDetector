#'Plays' mouse location in the 'terminal' - always results in a Visual Studio Crash

import pyautogui, sys
#import PySimpleGUI as sg

#Initially tried to get a pop up box with text to refresh - was not able to figure out
'''
layout = [  [sg.Text(pyautogui.position(), key='mymouseloc')],
            [sg.Button('OK')] ] 

window = sg.Window('Mouse Location', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == 'OK':
        window['mymouseloc'].update(values['mymouseloc'])


window.close
'''



#Instead have the position be recorded, then when clicked - record that position
#This was my attempt
'''
while True:
    print(pyautogui.position())

    if pyautogui.mouseDown() == True:
        print("You clicked!")
'''

#This is an example that works better from pyautogui.readthedocs
#Ctrl N to quit does not work
#print('Press Ctrl-C to quit.')
Click_Locations = []

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        if pyautogui.click()==True:
            Click_Locations.append(positionStr)
            print(Click_Locations)
            
            
except KeyboardInterrupt:
    print('\n')
    print("wow look cake!")