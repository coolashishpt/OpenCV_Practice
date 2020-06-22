import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread("messi5.jpg", cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img, cv.CV_64F, ksize= 3)
lap = np.uint8(np.absolute(lap))

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelCombined = cv.bitwise_or(sobelX, sobelY)
cannyedge = cv.Canny(img, 100, 200)

titles = ["image", "Laplacian", "SobelX", "SobelY", "SobelComined", "Canny"]
images = [img, lap, sobelX, sobelY, sobelCombined, cannyedge]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()