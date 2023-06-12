import cv2 as cv
import numpy as np

img = cv.imread('data/Chess.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray) # cornerHarris() function takes float32 image as input, so change the data type of the image to float32
dst = cv.cornerHarris(gray, 2, 3, 0.04) # 2-> block size(size of neighbourhood), 3-> sobel kernel size, 0.04-> k value in the equation

dst = cv.dilate(dst, None) # dilate the corner points to make them more visible

img[dst > 0.01 * dst.max()] = [0, 0, 255] # thresholding the image

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == ord('q'):
    cv.destroyAllWindows()
    
# Summary: Harris corner detector is a corner detection operator that is commonly used in computer vision algorithms to extract corners and infer features of an image. 