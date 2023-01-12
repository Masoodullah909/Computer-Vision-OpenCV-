# Joining two images

import cv2 as cv
import numpy as np

img = cv.imread("resources\img.jpg")

# Stacking Same Image

# 1- Horizontal Stack
hor_img = np.hstack((img, img))

# 2- Vertical Stack
ver_img = np.vstack((img, img))


cv.imshow("Horizontal Stack", hor_img)
cv.imshow("Vertical Stack", ver_img)

cv.waitKey(0)


# You can only stack images with same shape (width, height, color, channel)

(660, 500,3)