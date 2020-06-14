import cv2 as cv


cv.namedWindow("Messi")

def nothing(x):
    print(x)



cv.createTrackbar("CP", "Messi", 0, 255, nothing)


while(1):
    img = cv.imread("messi5.jpg")
    pos = cv.getTrackbarPos("CP", "Messi")

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 50), font, 1, (255, 255, 0), 2)

    if cv.waitKey(1) & 0xFF == 27: # Escape key for closing window
        break

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow("Messi", img)

cv.destroyAllWindows()