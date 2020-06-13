import cv2 as cv

img = cv.imread("messi5.jpg")
img2 = cv.imread("opencv-logo.png")

b, g, r = cv.split(img)

img = cv.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))

des = cv.addWeighted(img, .6, img2, .1, 0)


cv.imshow("Messi", des)
# cv.imshow("Opencv", img2)



cv.waitKey(0)
cv.destroyAllWindows()