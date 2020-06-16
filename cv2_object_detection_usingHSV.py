import cv2 as cv
import numpy as np

def nothing(x):
    pass

cam = cv.VideoCapture(0)
#for uses of camera 

cv.namedWindow("Tracker")
cv.createTrackbar("LH", "Tracker", 0, 255, nothing)
cv.createTrackbar("LS", "Tracker", 0, 255, nothing)
cv.createTrackbar("LV", "Tracker", 0, 255, nothing)
cv.createTrackbar("UH", "Tracker", 255, 255, nothing)
cv.createTrackbar("US", "Tracker", 255, 255, nothing)
cv.createTrackbar("UV", "Tracker", 255, 255, nothing)


while True:
    _, frame = cam.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH", "Tracking")
    l_s = cv.getTrackbarPos("LS", "Tracking")
    l_v = cv.getTrackbarPos("LV", "Tracking")

    u_h = cv.getTrackbarPos("UH", "Tracking")
    u_s = cv.getTrackbarPos("US", "Tracking")
    u_v = cv.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask= mask)

    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    cv.imshow("res", res)

    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()