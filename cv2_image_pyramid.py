import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.jpg")
lr1 = cv.pyrDown(img) # lower the resolution 1
lr2 = cv.pyrDown(lr1) # lower the resolution 2

hr1 = cv.pyrUp(lr2)

cv.imshow("Original", img)
cv.imshow("pyrDown 1 Image", lr1)
cv.imshow("pyrDown 2 Image", lr2)
cv.imshow("pyrUp 1 Image", hr1)

cv.waitKey(0)
cv.destroyAllWindows()
