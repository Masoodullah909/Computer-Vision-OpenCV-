# Converting Video CAM to Grayscale and Binary


import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0)  # Webcame no.1

while(True):
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)


    cv.imshow("Orignal Cam", frame)
    cv.imshow('Gray Cam', gray_frame)
    cv.imshow('Binary Cam', binary)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
     