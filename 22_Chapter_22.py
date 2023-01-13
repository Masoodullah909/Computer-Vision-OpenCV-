# Face Detection in images using OpenCV

import cv2 as cv

face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')





# Reading the image
img = cv.imread('resources/faces.jpeg')
# print(img.shape)

# Resizing the image
# img = cv.resize(img, (480, 640))
# print(img.shape)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

# Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)



cv.imshow('Images', img)
cv.waitKey(0)
cv.destroyAllWindows()
