import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((200, 200), np.uint8) 
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)

img = cv.imread('data/Me.jpg', -1)

b, g, r = cv.split(img)

cv.imshow('Image', img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

hist = cv.calcHist([img], [0], None, [256], [0, 256]) # [0] is the channel, None is the mask, [256] is the number of bins, [0, 256] is the range of values
plt.plot(hist)
plt.show()

plt.hist(img.ravel(), 256, [0, 256]) # ravel() is used to flatten the array, 256 is the number of bins, [0, 256] is the range of values
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()