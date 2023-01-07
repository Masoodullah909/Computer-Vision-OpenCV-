# Reading an image and displaying it 
# Library import
import cv2 as cv

img = cv.imread("resources\image.jpg")

cv.imshow("Pehli Image", img)
cv.waitKey(0)

