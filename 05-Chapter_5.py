# Image Saving and Image Writting

# Import Library
import cv2 as cv

# Read Image
img = cv.imread('resources/image.jpg')

# # Resize Image
# img = cv.resize(img, (500, 600))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)


cv.imwrite('resources/gray.jpg', gray)
cv.imwrite('resources/binary.jpg', binary)

