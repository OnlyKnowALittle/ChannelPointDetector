#Sentdex code for 'OpenCV' face detection with Haar Cascade
#Trying to figure this out so I can then try to duplicate the face and paste in an image
#1st problem - cascadeclassifier supposedly is part of the cv2 package but for some reason I needed to download frontalface
#also must use 'from cv2 import cv2', 'import cv2' alone doesn't work

import numpy as np
from cv2 import cv2

#Data Files
#multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

face_cascade = cv2.CascadeClassifier('C:/Users/billt/Documents/Python/haarcascade_frontalface_default.xml')

#face_cascade = cv2.CascadeClassifier('C:/Users/billt/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/datahaarcascade_frontalface_default.xml')
#wont work because of multiscale errors?

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#not using cause don't need eyes

#Camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
