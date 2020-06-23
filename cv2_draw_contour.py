import cv2 as cv

img = cv.imread("opencv.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of contours =" + str(len(contours)))
print(contours[0])

cv.drawcontours(img, contours, -1, (0,255, 0), 3)

cv.imshow("Image", img)
cv.imshow("Image GRAY", imgray)
cv.waitKey(0)
cv.destroyAllWindows()
