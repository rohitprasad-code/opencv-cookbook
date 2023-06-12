import cv2 as cv
import numpy as np

# https://github.com/opencv/opencv/tree/4.x/data/haarcascades -> haarcascade
# haarcascade -> means haar classifier which is used to detect the object in an image

face_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('data/haarcascade_eye_tree_eyeglasses.xml')

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    # classifier works on gray scale image
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # faces-> vector of rectangles where each rectangle contains the detected object

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x: x+w]
        roi_color = frame[y:y+h, x: x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # draw rectangle on the eyes
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()
