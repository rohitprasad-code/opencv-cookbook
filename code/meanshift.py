import cv2 as cv
import numpy as np

cap = cv.VideoCapture('data/Road-traffic-demo.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
x, y, w, h = 95, 425, 145, 55
track_window = (x, y, w, h)

# set up the ROI for tracking
roi = frame[y:y+h, x:x+w]

# set up the ROI histogram for tracking
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# set up the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 4)

cv.imshow('roi', roi)
while True:
    ret, frame = cap.read()
    
    if ret == True:
        
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)
        # draw it on image
        x, y, w, h = track_window
        final_image = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 3)
        
        cv.imshow('dst', dst)
        cv.imshow('final_image', final_image)
        k = cv.waitKey(30) & 0xff
        if k == ord('q'):
            break
    else:
        break
