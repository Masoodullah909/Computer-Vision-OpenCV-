# Co-ordinates of an image or video

# Step-1 Import Libraries
import cv2 as cv
import numpy as np

# Step-2 Define a function
def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        # left mouse clicks
        print(x,'',y)
        # How to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' + str(y), (x,y), font, 1, (255,0,0), thickness=2)
        # show the text on image and img itself
        cv.imshow('image', img)

    # For Color Finding
    if event == cv.EVENT_RBUTTONDOWN:
        print(x,'', y)

        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        
        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (0,25,55), thickness=2)
        cv.imshow('image', img)



# Final Function to read or display an image
if __name__=="__main__":
    # Read an image
    img = cv.imread('resources\perspective.jpg', 1)
    # display an image
    cv.imshow('image', img)
    # Setting call back function
    cv.setMouseCallback('image', find_coord)
    # wait for a key to be pressed
    cv.waitKey(0)
    # close all windows
    cv.destroyAllWindows()
    


