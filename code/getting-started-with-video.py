import cv2

cap = cv2.VideoCapture(0) # 0 for default camera, 1 for second camera, etc.
                          # can also pass in a video file with the path to the file
                          
fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc is a 4-byte code used to specify the video codec and also write it as 'X', 'V', 'I', 'D'
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) # saves the video 
                                                                # 'output.avi' is the name of the file
                                                                # fourcc is the codec           
                                                                # 20.0 is the number of frames per second
                                                                # (640, 480) is the width and height of the frame
                          
while(cap.isOpened()): # checks if the camera is opened correctly
    ret, frame = cap.read() # ret is a boolean that returns true if the frame is read correctly
    
    if ret == True:
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # gets the width of the frame
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # gets the height of the frame

        out.write(frame) # writes the frame to the file
        
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts the frame to grayscale

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): # 0xFF is a mask to get the last 8 bits and 1 is the wait time
            break
    else:
        break

cap.release() # releases the capture
out.release() # releases the output
cv2.destroyAllWindows()