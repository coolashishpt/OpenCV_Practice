import cv2 as cv

# capture
cam = cv.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv.imshow("Camera", frame)
    if cv.waitkey(1) & 0xFF == ord("q"):
        break

cam.release()
cv.destroyAllWindows()

