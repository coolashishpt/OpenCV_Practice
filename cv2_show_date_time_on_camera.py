import cv2 as cv
import datetime as dt

cam = cv.VideoCapture(0)

print(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cam.get(cv.CAP_PROP_FRAME_WIDTH))

# cam.set(3, 3000)
# cam.set(4, 3000)
#
# print(cam.get(3))
# print(cam.get(4))
while(True):

    ret, frame = cam.read()

    font = cv.FONT_ITALIC
    test = str(dt.datetime.now()) + str(" \nAshish Prasad")

    frame = cv.putText(frame, test, (10, 50), font, 0.7,
                       (0, 0, 0), 2, cv.LINE_AA)

    cv.imshow("Camera", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv.destroyAllWindows()