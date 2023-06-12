import cv2 as cv
import numpy as np

img = cv.imread('data/Colored-ball.jpg')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.5, 10)
detected_circles = np.uint16(np.around(circles))
for (x, y ,r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3)
    cv.circle(output, (x, y), 2, (0, 255, 255), 3)
    
cv.imshow('image', img)
cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()

# (x - center_x)^2 + (y - center_y)^2 = radius^2

# HoughCircles->it is used to detect circles in an image