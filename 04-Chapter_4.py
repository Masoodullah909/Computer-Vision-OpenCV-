# Image into Black and White Image

import cv2 as cv

img = cv.imread('resources\image.jpg')
img = cv.resize(img, (500, 600))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, blackAndWhiteImage) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

cv.imshow('original', img)
cv.imshow('gray', gray)
cv.imshow('black and white', blackAndWhiteImage)

cv.waitKey(0)
cv.destroyAllWindows()