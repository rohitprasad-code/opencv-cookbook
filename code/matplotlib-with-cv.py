import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('data\Me.jpg', -1)  # OPENCV reads image in BGR format

cv.imshow('Image', img)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(img)                     # MATPLOTLIB reads image in RGB format
plt.title('BGR')

# Convert BGR to RGB using cvtColor() method
plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('RGB')

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

