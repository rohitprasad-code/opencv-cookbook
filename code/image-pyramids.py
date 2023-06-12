import cv2 as cv
import numpy as np

img = cv.imread('data/Me.jpg', -1)

# Gaussian Pyramid
# lowering the resolution of the image
lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)
# increasing the resolution of the image
hr1 = cv.pyrUp(lr2)
hr2 = cv.pyrUp(hr1)

cv.imshow('Original Image', img)
cv.imshow('PyrDown Image 1', lr1) 
cv.imshow('PyrDown Image 2', lr2)
cv.imshow('PyrUp Image 1', hr1)
cv.imshow('PyrUp Image 2', hr2)

cv.waitKey(0)
cv.destroyAllWindows()
 
# Two types of image pyramids:
#   1. Gaussian Pyramid
#   2. Laplacian Pyramid

# Laplacian Pyramid has no exclusive function in OpenCV

