import cv2 as cv
import numpy as np

img = cv.imread('data/Logo.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgGray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 

print('Number of contours: ' + str(len(contours)))
print(contours[0])

cv.drawContours(img, contours, -1, (0, 255, 0), 3) # -1 means all contours

cv.imshow('Image', img)
cv.imshow('Gray Image', imgGray)
cv.imshow('Gray Image', imgGray)
cv.waitKey(0)
cv.destroyAllWindows()

# Contours are the boundaries of a shape with same intensity 