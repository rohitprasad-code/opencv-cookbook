import cv2 as cv
import numpy as np

img = cv.imread('data/Polugon-shape.png')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10) # 100-> maxCorners, 0.01-> qualityLevel, 10-> minDistance

corners = np.int0(corners) # convert the corners to integers

for i in corners:
    x, y = i.ravel() # ravel() function returns a contiguous flattened array
    cv.circle(img, (x, y), 3, (0, 0, 255), -1) # draw a circle at each corner point
    

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == ord('q'):
    cv.destroyAllWindows()
    
    
# Summary: Shi-Tomasi corner detector is a modification of Harris corner detector. It gives better results than Harris corner detector. It is also called as goodFeaturesToTrack() function. In this we can control the number of corners we want to detect. It is more appropriate for tracking.