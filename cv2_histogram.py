import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("lena.jpg")



hist = cv.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)

plt.show()





cv.waitKey(0)
cv.destroyAllWindows()
