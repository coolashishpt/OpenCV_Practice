import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("salt_paper_noise.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernal = np.ones((5,5), np.float32)/25

dst = cv.filter2D(img, -1, kernal)
blur = cv.blur(img, (5,5))
gblur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)


title = ["Original", "dst", "blur", "gblur", "median", "bilateralFilter"]
images = [img, dst, blur, gblur, median, bilateralFilter]



for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
    
