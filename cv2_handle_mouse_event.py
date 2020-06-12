import cv2 as cv
import numpy as np
event  = [i for i in dir(cv) if "EVENT" in i]
print(event)

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv.FONT_ITALIC
        text = str(x) + ", " + str(y)
        cv.putText(img, text, (x, y), font, 1, (255, 255, 0), 1)
        cv.imshow("Image", img)

    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        textrgb = str(blue) + ", " + str(green) + ", " + str(red)
        font = cv.FONT_ITALIC

        cv.putText(img, textrgb, (x, y), font, 1, (0, 255, 255), 1)
        cv.imshow("Image", img)

img = np.zeros((512, 512, 3), np.uint8)

cv.imshow("Image", img)

cv.setMouseCallback("Image", click_event)

if cv.waitKey(0) & 0xFF == ord("q"):
    cv.destroyAllWindows()

# cv.waitKey(0)
# cv.destroyAllWindows()