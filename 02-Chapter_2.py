# Resizing an Image

# Library import
import cv2 as cv

# Reading an image
img = cv.imread("resources\image.jpg")
# Resize and Image
img1= cv.resize(img, (600, 800))

# Displaying an Image
cv.imshow("First Image", img)
cv.imshow("Second Image", img1)

cv.waitKey(0)
cv.destroyAllWindows()
