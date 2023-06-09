import numpy as np
import cv2

# img = cv2.imread('data/Me.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8) # creates a black image

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5) # draws a line from (0, 0) to (255, 255) with color (bgr)->(255, 0, 0) and thickness 5

img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 5) # draws an arrowed line

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5) # draws a rectangle
# if thickness is -1, then the rectangle is filled

img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1) # draws a circle with center (447, 63) and radius 63 

img = cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA) # puts text on the image

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()