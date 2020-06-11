import numpy as np
import cv2 as cv

img = np.zeros([512, 512, 3])

img = cv.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
img = cv.arrowedLine(img, (0, 255), (255, 255), (0, 0, 255), 8)

font = cv.FONT_ITALIC
img = cv.putText(img, "OpenCV", (10, 500), font, 4, (0, 255, 255), 10, cv.LINE_AA)

cv.imshow("Numpy Image", img)

cv.waitKey(0)

