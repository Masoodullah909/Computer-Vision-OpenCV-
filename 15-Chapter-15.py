# Resolution of cam

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Resolution Full HD (1920x1080)
def full_hd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)

# Resolution HD (1280x720)
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)

# Resolution SD/ VGA (640x480)
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)

# Resolution QVGA (320x240)
def qvga_resolution():
    cap.set(3, 320)
    cap.set(4, 240)



qvga_resolution()   


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv.imshow('frame', frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()



    