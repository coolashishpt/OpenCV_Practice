import cv2 as cv

cam = cv.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv.imshow("Camera", frame)
    cv.waitKey(0)

