import cv2 as cv

img = cv.imread("gradient.png")

cv.imshow("Image", img)

th1 = 

cv.waitKey(0)
cv.destroyAllWindows()