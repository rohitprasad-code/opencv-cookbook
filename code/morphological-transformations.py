import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/Colored-ball.jpg', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV) # covert image to binary

# dilation-> add pixels to the boundaries of objects in an image
kernel = np.ones((2, 2), np.uint8)                  # kernel-> matrix of ones
dilation = cv.dilate(mask, kernel, iterations=3)    # iterations-> how many times to apply dilation

# erosion-> remove pixels at the boundaries of objects in an image
erosion = cv.erode(mask, kernel, iterations=3)

# opening-> erosion followed by dilation
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

# closing-> dilation followed by erosion
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

# gradient-> difference between dilation and erosion of an image
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)

# tophat-> difference between input image and opening of the image
tophat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat'] 
images = [img, mask, dilation, erosion, opening, closing, gradient, tophat]

for i in range(len(titles)):
    plt.subplot(1, len(titles), i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
