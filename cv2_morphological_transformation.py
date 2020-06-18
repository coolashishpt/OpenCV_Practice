import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("smarties.png", cv.IMREAD_GRAYSCALE)

_, mask = cv.threshold(img, 220, 250, cv.THRESH_BINARY)

filter = np.zeros((5,5), np.uint8)

dilation = cv.dilate(mask, filter, iterations= 2) 
erosion = cv.erode(mask, filter, iterations= 2)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, filter)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, filter)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, filter)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, filter)

title = ["Original", "dilation", "erosion", "opening", "closing", "mg", "th"]
images = [img, dilation, erosion, opening, closing, mg, th]


fig = plt.figure(figsize=(12,12))
for i in range(len(images)):
    fig.add_subplot(3, 3, i+1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()