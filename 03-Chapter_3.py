# Grayscale Conversion


# Import libraries
import cv2 as cv

# Loading and Resizing Image
img = cv.imread('resources\image.jpg')
img = cv.resize(img, (600, 700))

# Grayscale Conversion
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# display code
cv.imshow('BGR Image', img)
cv.imshow('Grayscale Image', gray_img)

# Delay code
cv.waitKey(0)
cv.destroyAllWindows()