# How to change the perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread('resources\perspective.jpg')
print(img.shape)
reshape_img = cv.resize(img, (800,900))
print(reshape_img.shape)



# Defining Point
point1 = np.float32([[233, 196],[82,471] , [522,169],[715,482]])
width = 800
height = 900
width , height = 800,900

point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(reshape_img, matrix, (width, height))

cv.imshow("orignal", reshape_img)
cv.imshow("output", out_img)

cv.imwrite("resources\Wrap_Prespective.jpg", out_img)


cv.waitKey(0)
cv.destroyAllWindows()