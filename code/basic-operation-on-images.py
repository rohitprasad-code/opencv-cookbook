import cv2
import numpy as np

img = cv2.imread('data/Me.jpg', -1)
img2 = cv2.imread('data/Logo.png', -1)

print(img.shape)    # returns a tuple of number of rows, columns and channels
print(img.size)     # returns total number of pixels is accessed
print(img.dtype)    # returns image datatype is obtained

b, g, r = cv2.split(img)    # split image into its b, g, r channels
# cv2.imshow('b', b)        # show b channel
# cv2.imshow('g', g)        # show g channel
# cv2.imshow('r', r)        # show r channel
img = cv2.merge((b, g, r))  # merge b, g, r channels back into img

face = img[569:990, 444:829] # img[y1:y2, x1:x2]
img[0:421, 0:385] = face

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

# dst = cv2.add(img, img2)    # add two images
dst = cv2.addWeighted(img, .9, img2, .4, 0) # add two images with weights (img1, weight1, img2, weight2, gamma)
cv2.imshow('dst', dst)

img = cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()