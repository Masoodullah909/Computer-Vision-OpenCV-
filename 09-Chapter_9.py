# How to capture a webcame inside python

# step-1: Import Libraries
import cv2 as cv
import numpy as np

# Step-2: Read the frame from the webcame
cap = cv.VideoCapture(0)  # Webcame no.1

# Read untill the end
# Step-3: Display the frame by frame
while(cap.isOpened()):
    # capture frame by frame 
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv.imshow('Frame', frame)
        # Press q to exit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release and close window easily
cap.release()
cv.destroyAllWindows()