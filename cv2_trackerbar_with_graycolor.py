import cv2 as cv


cv.namedWindow("Messi")

def nothing(x):
    print(x)



cv.createTrackbar("CP", "Messi", 10, 400, nothing)

switch = "color/gray"
cv.createTrackbar(switch, "Messi", 0, 1, nothing)

while(1):
    img = cv.imread("messi5.jpg")
    pos = cv.getTrackbarPos("CP", "Messi")

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 50), font, 1, (255, 255, 0), 2)

    if cv.waitKey(1) & 0xFF == 27: # Escape key for closing window
        break

    s = cv.getTrackbarPos(switch, "Messi")

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow("Messi", img)

cv.destroyAllWindows()