# Library import
import cv2 as cv

img = cv.imread("/workspaces/Computer-Vision-OpenCV-/resources/image.jpg")

cv.imshow("Pehli Image", img)
cv.waitKey(0)