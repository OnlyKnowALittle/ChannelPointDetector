#channelpoints - pyautolocates the channel point image and prints the location
import pyautogui
from PIL import Image
import pytesseract
#Following three lines allow for searching of both monitors - without pyautogui only looks at left screen
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

#Locate the bubble on screen and print location - currently detects the bubble on my screen and not just in chat
def FindBubbles():
    pointslocation = pyautogui.locateOnScreen(r'E:/Projects/Python/Twitch_Points/Point_Dot_Color.png')
    pointscenter = pyautogui.locateCenterOnScreen(r'E:/Projects/Python/Twitch_Points/Point_Dot_Color.png')
    print(pointslocation)
    print(pointscenter)
    myScreenshot = pyautogui.screenshot(region=(pointslocation))
    myScreenshot.save(r'E:/Projects/Python/Twitch_Points/test.png')

#FindBubbles()
img = Image.open('E:/Projects/Python/Twitch_Points/NumberTest.jpg')
print(pytesseract.image_to_string(img, config='--psm 6'))
#numbershow = get_text(img)

'''
#(region=(0,0, 300, 400))
#left, top, width, and height
#mycake = pyautogui.screenshot(region=(1920,200, 400, 160))
#mycake.save(r'E:/Projects/Python/Twitch_Points/region.png')


-Screenshot region and find picture
https://pyautogui.readthedocs.io/en/latest/screenshot.html
-Multiple Monitor Solution
https://github.com/asweigart/pyautogui/issues/321
-Select Text
https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/
'''