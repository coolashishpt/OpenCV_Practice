import numpy as np
import cv2 as cv

img = np.zeros((300, 512, 3), np.uint8)

cv.namedWindow("Image Trackbar")


def nothing(x):
    print(x)


cv.createTrackbar("B", "Image Trackbar", 0, 255, nothing)
cv.createTrackbar("G", "Image Trackbar", 0, 255, nothing)
cv.createTrackbar("R", "Image Trackbar", 0, 255, nothing)

switch = "0: OFF\n 1: ON"
cv.createTrackbar(switch, "Image Trackbar", 0, 1, nothing)

while(1):
    cv.imshow("Image Trackbar", img)
    if cv.waitKey(1) & 0xFF == 27: # Escape key for closing window
        break

    b = cv.getTrackbarPos("B", "Image Trackbar")
    g = cv.getTrackbarPos("G", "Image Trackbar")
    r = cv.getTrackbarPos("R", "Image Trackbar")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()
