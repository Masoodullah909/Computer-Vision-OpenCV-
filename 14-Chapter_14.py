# How to Draw Lines, and shape in python

import cv2 as cv
import numpy as np

# Draw a canvas
img = np.zeros((600,600)) # 0's for Black
# img1 = np.ones((600,600)) # 1's for White

# print size 
print("The Size of Image is:", img.shape)
# print(img)

# Adding colors to the canvas
colored_img = np.zeros((600,600,3), np.uint8) # 3 for RGB
colored_img[:] = 245, 210, 200 # BGR

# Colored inside a canvas
colored_img[150:230, 100:207] = 255, 0, 0 # BGR

# Adding a line
cv.line(colored_img, (0,0), (colored_img.shape[0],colored_img.shape[1]),(255,0,0), 3) # Full line
cv.line(colored_img, (100,100), (300,300),(255,255,50), 3)  # Part line

# Adding a rectangle
cv.rectangle(colored_img, (50,100), (300,400), (255,240,0), 2) # Draw rectangle
cv.rectangle(colored_img, (50,100), (300,400), (255,240,0), cv.FILLED) # Filled rectangle

# Adding a circle
cv.circle(colored_img, (300,300), 50, (255,100,0),  5) # Draw circle
cv.circle(colored_img, (400,300), 50, (255,100,0),  cv.FILLED) # Filled circle

# Adding a text
cv.putText(colored_img, "Masood Ullah", (200,500), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,0), 2 )



# cv.imshow("Black Canvas", img)
# cv.imshow("White Canvas", img1)
cv.imshow("Colored Canvas", colored_img)
cv.waitKey(0)
cv.destroyAllWindows()