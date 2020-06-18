import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("sudoku.png", 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

title = ["Original", "Thresh Binary", "Adaptive Mean", "Adaptive Gaussian"]
images = [img, th1, th2, th3]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])


plt.show()
# cv.imshow("Image", img)
# cv.imshow("th1", th1)
# cv.imshow("th2", th2)
# cv.imshow("th3", th3)

# cv.waitKey(0)
# cv.destroyAllWindows()
