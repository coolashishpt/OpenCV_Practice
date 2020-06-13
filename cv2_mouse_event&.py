import numpy as np
import cv2 as cv


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), 3, (0, 0, 255), -1)
        point.append((x, y))

        if len(point) >= 2:
            cv.line(img, point[-1], point[-2], (255, 0, 0), 5)

        cv.imshow("Image", img)

    elif event == cv.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]


        cv.circle(img, (x, y), 3, (255, 123, 0), 1)
        myimage = np.zeros((548, 342, 3), np.uint8)
        myimage[:] = [blue, green, red]

        cv.imshow("Color", myimage)


# img = np.zeros((512, 512, 3))
img = cv.imread("messi5.jpg")
point = []

cv.imshow("Image", img)
cv.setMouseCallback("Image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()
