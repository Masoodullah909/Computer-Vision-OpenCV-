# Writing/ Recording Videos from Cam

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)  # Webcame no.1

# Writting Format, codec, video writer and file output
fram_width = int(cap.get(3))
fram_height = int(cap.get(4))

out = cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (fram_width, fram_height))  #isColor=False for gray scale

while(True):
    (ret, frame) = cap.read()
    # gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # To show in player
    if ret == True:
        out.write(frame)
        # out.write(gray_frame)
        cv.imshow("Orignal Cam", frame)
        cv.imshow('Gray Cam', gray_frame)
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv.destroyAllWindows()