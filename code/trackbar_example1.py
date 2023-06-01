import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B','image', 0, 255, nothing) # parameters: trackbarName, windowName, default-value, count, onChange
cv.createTrackbar('G','image', 0, 255, nothing)
cv.createTrackbar('R','image', 0, 255, nothing)

switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF    # 0xFF is a hexadecimal constant which is 11111111 in binary.
    if k == 27:
        break
    
    b = cv.getTrackbarPos('B','image') # parameters: trackbarName, windowName
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
    
cv.destroyAllWindows()