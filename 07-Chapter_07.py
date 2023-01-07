# Converting Video to gray and Black and White

import cv2 as cv

cap = cv.VideoCapture('resources/video.mp4')

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    # To show in Player
    if ret == True:
        #   cv.imshow('Video', frame)
        cv.imshow('Gray Video', grayframe)
        # cv.imshow('Binary Video', binary)
        
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 



cap.release()
cap.destroyAllWindows()