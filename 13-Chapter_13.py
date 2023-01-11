# Basic Functions or Manipulation in opencv

import cv2 as cv
import numpy as np

img = cv.imread("resources\image.jpg")
# To Check Image Size
print("The Shape of Original Image is:",img.shape)

# Resize
resized_img = cv.resize(img, (250, 450))

# Gray 
gray_img = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)

# Black and white
(thresh, black_white) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

# Blurred Image
blur_img = cv.GaussianBlur(resized_img, (7, 7), 0)

# Edge Detection
edge_img = cv.Canny(resized_img, 47, 47)

# Thickness of Lines
# dilated_img = cv.dilate(edge_img, (7,7), iterations=1)
mat_kernel = np.ones((7,7), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel), iterations=1)

# Errosion (Make thiner Outline)
ero_img = cv.erode(dilated_img, (mat_kernel), iterations=1)

# Crop Image
# We will use numpy library not open cv
crop_img = resized_img[0:200, 200:500]



cv.imshow("Original", img)
cv.imshow("Resized", resized_img)
cv.imshow("Black and Whit", black_white)
cv.imshow("Gray", gray_img)
cv.imshow("Blur", blur_img)
cv.imshow("Edge", edge_img)     
cv.imshow("Dilated", dilated_img)
cv.imshow("Erosion", ero_img)
cv.imshow("Crop", crop_img)

cv.waitKey(0)
cv.destroyAllWindows()