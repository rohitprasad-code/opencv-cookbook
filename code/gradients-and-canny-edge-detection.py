import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/Sudoku.jpg', cv.IMREAD_GRAYSCALE)

# Laplacian gradient -> second derivative which is more sensitive to edges
lap = cv.Laplacian(img, cv.CV_64F, ksize=1) # parameter cv.CV_64F is the data type
lap = np.uint8(np.absolute(lap)) # convert to unsigned 8-bit integer

# Sobel gradient -> first derivative
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0) # parameter 1, 0 is the order of the derivative in x and y direction respectively
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1) # parameter 0, 1 is the order of the derivative in x and y direction respectively

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv.bitwise_or(sobelX, sobelY)

# Cannny edge -> uses sobel gradient internally to detect edges
canny = cv.Canny(img, 100, 200) # 100 low threshold, 200 high threshold

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(len(titles)):
    plt.subplot(1, len(titles), i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()  


# Summary:

# The canny edge detection algm is composed of 5 steps:
#     1. Noise reduction
#     2. Gradient calculation
#     3. Non-maximum suppression
#     4. Double threshold
#     5. Edge tracking by hysteresis

# laplacian gradient is more sensitive to edges than sobel gradient
# But both are not good at detecting edges in noisy images