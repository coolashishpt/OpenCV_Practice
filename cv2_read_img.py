import cv2 as cv
img = cv.imread("F:\OpenCV\messi5.jpg", -1)
print(img)
cv.imshow("image", img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord("s"):
    cv.imwrite("new_messi.jpg", img)