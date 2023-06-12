import cv2 as cv
import numpy as np

cap = cv.VideoCapture('data/Road-traffic.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2) # absolute difference between frame1 and frame2
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY) # convert to 
    blur = cv.GaussianBlur(gray, (5, 5), 0) # remove noise
    _, thresh = cv.threshold(blur, 30, 255, cv.THRESH_BINARY) # threshold the image
    dilated = cv.dilate(thresh, None, iterations=3) # dilate the image
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # find contours
    
    # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2) # draw contours on frame1
    
    # draw rectangles around moving objects
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 1000:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame1, 'Status: {}'.format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv.imshow('Video', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()