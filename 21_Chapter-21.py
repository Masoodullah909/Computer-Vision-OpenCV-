# How to detect specific color inside python

import cv2 as cv
import numpy as np

# img = cv.imread('resources/img.jpg')

# # Convert the image to HSV (Hue, Saturation, Value)
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Sliders to adjust the HSV values
def slider():
    pass

path = 'resources/perspective.jpg'

cv.namedWindow('Bars')
cv.resizeWindow('Bars', 540, 340)

cv.createTrackbar('Hue Min', 'Bars', 0, 179, slider)
cv.createTrackbar('Hue Max', 'Bars', 179, 179, slider)

cv.createTrackbar('Sat Min', 'Bars', 0, 255, slider)
cv.createTrackbar('Sat Max', 'Bars', 255, 255, slider)

cv.createTrackbar('Val Min', 'Bars', 0, 255, slider)
cv.createTrackbar('Val Max', 'Bars', 255, 255, slider)


img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# hue_min = cv.getTrackbarPos('Hue Min', 'Bars')
# print(hue_min)

while True:
    img - cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos('Hue Min', 'Bars')
    hue_max = cv.getTrackbarPos('Hue Max', 'Bars')
    sat_min = cv.getTrackbarPos('Sat Min', 'Bars')
    sat_max = cv.getTrackbarPos('Sat Max', 'Bars')
    val_min = cv.getTrackbarPos('Val Min', 'Bars')
    val_max = cv.getTrackbarPos('Val Max', 'Bars')
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    # To see these changes inside an image, we need to create a mask
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img, mask=mask_img)


    # cv.imshow('Original', img)
    # cv.imshow('HSV', hsv_img)
    cv.imshow('Mask', mask_img)
    cv.imshow('Output', out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()



