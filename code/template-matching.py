import cv2 as cv
import numpy as np

img = cv.imread('data/Me.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('data/Me-face.jpg', 0)
w, h = template.shape[::-1] # [::-1] is used to reverse the array

result = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
print(result)
threshold = 0.95
loc = np.where(result >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
