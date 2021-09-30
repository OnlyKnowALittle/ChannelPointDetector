#Youtube 'click' program. opens firefox from location click then uploads with user input info and more clicking
#Dumb Click Program

import pyautogui, sys, time
import PySimpleGUI as sg


layout = [  [sg.Text('Video Location')], [sg.FileBrowse(key='location'),],
            [sg.Text('Video Title')], [sg.Multiline(size=(30, 5), key='textbox')],
            [sg.Text('Video Description')], [sg.Multiline(size=(30, 5), key='description')], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Video Uploader', layout)

event, values = window.read()

window.close()

'''
sg.popup(f"{values['textbox'][:]}")
sg.popup(f"{values['location'][:]}")
sg.popup(f"{values['description'][:]}")


#print(values['textbox'])
#print(values['location'])
'''

def sequence_time():
    #opening firefox - going to Youtube
    pyautogui.click(525, 1058)
    time.sleep(2)
    pyautogui.hotkey('y', 'o', 'enter')

    #Click Upload
    pyautogui.click(1644, 133)
    pyautogui.click(1644, 207)
    
    #Clicking Select File
    pyautogui.click(944,702)
    pyautogui.click(598,54)
    pyautogui.write(f"{values['location'][:]}")
    pyautogui.click(222,174)

    #Title
    pyautogui.click(654, 420)
    pyautogui.write(f"{values['textbox'][:]}")

    #Description
    pyautogui.click(654, 564)
    pyautogui.write(f"{values['description'][:]}")

    #Thumbnail
    pyautogui.click(551, 803)
    #click - write(thumbnail location) in directory - click top left area
    #could get where the thumbnail is at first step from user but have to get directory with file name - take away file name - go to just directory - search for file name - select


#sequence_time()
