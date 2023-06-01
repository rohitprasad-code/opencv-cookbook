import cv2

img = cv2.imread('Me.jpg', 0) # 0 for grayscale, 1 for color, -1 for unchanged

# prints the array of pixels
print(img) 

# shows the image
cv2.imshow('image', img)

# waits
key = cv2.waitKey(5000) # 0 for infinite, 5000 for 5 seconds, etc.

if key == 27: # 27 is the escape key
    cv2.destroyAllWindows()
elif key == ord('s'): # ord() returns the unicode value of the character
    cv2.imwrite('MeGray.jpg', img) # saves the image
    cv2.destroyAllWindows()
    
    
# Summary: 1. Load and show image
#          2. Wait for key press
#          3. idea: if key is escape, close window else if key is s, save image and close window