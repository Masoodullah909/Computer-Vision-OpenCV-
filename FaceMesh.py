import cv2 as cv
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    cv.imshow("Image", img)
    cv.waitKey(1)