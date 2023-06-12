import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2() 
# MOG-> mixture of gaussian & MOG2-> mixture of gaussian with adaptive thresholding. 
# MOG2 is better than MOG
# In MOG2, we can set the learning rate and shadow detection

while True:
    ret, frame = cap.read()
    if frame is None:
        break
        
    fgmask = fgbg.apply(frame)
    
    cv.imshow('frame', frame)
    cv.imshow('FG frame', fgmask)
    
    if cv.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()