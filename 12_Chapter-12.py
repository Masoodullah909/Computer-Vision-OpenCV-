# Setting of camera or video

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)  # Webcame no.1

cap.set(10, 50) # 10 is brightness, 50 is value
cap.set(3, 640) # 3 is width, 64 is value
cap.set(4, 480) # 4 is height, 48 is value

while (True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
