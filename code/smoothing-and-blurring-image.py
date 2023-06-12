import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/Sudoku.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25

# filter2D-> convolves an image with the kernel
dst = cv.filter2D(img, -1, kernel) # -1-> depth of the destination image

# blur-> convolves an image with a normalized box filter
blur = cv.blur(img, (5, 5))

# GaussianBlur-> convolves an image with a Gaussian kernel
gaussianBlur = cv.GaussianBlur(img, (5, 5), 0) # 0-> sigmaX

# salt and pepper noise

# medianBlur-> applies a median blur to an image
medianBlur = cv.medianBlur(img, 5)

# bilateralFilter-> applies a bilateral filter to an image
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)
# used for noise removal while keeping edges sharp
 
titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'medianBlur', 'bilateralFilter'] 
images = [img, dst, blur, gaussianBlur, medianBlur, bilateralFilter]

for i in range(len(titles)):
    plt.subplot(1, len(titles), i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()