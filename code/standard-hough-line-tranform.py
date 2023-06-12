import cv2 as cv
import numpy as np

img = cv.imread('data/Sudoku.jpg')

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(grey, 0, 150, apertureSize=3) # parameters: source_image, min_threshold, max_threshold, aperture_size
lines = cv.HoughLines(edges, 1, np.pi/180, 200) # parameters: source_image, distance_resolution, angle_resolution, threshold

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0, y0 = a*rho, b*rho
    # x1 stores the rounded off value of (r*cos(theta) - 1000*sin(theta))
    # y1 stores the rounded off value of (r*sin(theta) + 1000*cos(theta))
    x1, y1 = int(x0 + 1000*(-b)), int(y0 + 1000*(a))
    # x2 stores the rounded off value of (r*cos(theta) + 1000*sin(theta))
    # y2 stores the rounded off value of (r*sin(theta) - 1000*cos(theta))
    x2, y2 = int(x0 - 1000*(-b)), int(y0 - 1000*(a))

    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv.imshow('canney', edges)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Hough Tranform Basics
# Hough Transform is a popular technique to detect any shape, if you can represent that shape in mathematical form. It can detect the shape even if it is broken or distorted a little bit. We will see how it works for a line.

# In Cartesian coordinates system
#     y = mx + c
# In Polar coordinates system
#     x cos(theta) + y sin(theta) = r

# Steps involved in Hough Transform:
#     1. Edge detection e.g. using the canny edge detector
#     2. Mapping of edge points to the Hough space and storage in an accumulator
#     3. Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding and possibly other constraints
#     4. Conversion of infinite lines to finite lines

# OpenCV implements two kind of Hough Line Transforms
#     1. The Standard Hough Transform (HoughLines method)
#     2. The Probabilistic Hough Line Transform (HoughLinesP method)
