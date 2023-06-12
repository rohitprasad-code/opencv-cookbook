import cv2 as cv
import numpy as np

img = cv.imread('data/images.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 100, 150, apertureSize=3)
cv.imshow('edges', edges)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)  # parameters: source_image, distance_resolution, angle_resolution, threshold, min_line_length, max_line_gap, lines=None
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()