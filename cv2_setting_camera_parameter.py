import cv2 as cv

cam = cv.VideoCapture(0)
print(cam.isOpened())

print(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cam.get(cv.CAP_PROP_FRAME_WIDTH))

cam.set(3, 1280)  # 3 for Height
cam.set(4, 720)  # 4 for Width

print(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cam.get(cv.CAP_PROP_FRAME_WIDTH))

while(True):

    ret, frame = cam.read()

    cv.imshow("Camera", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv.destroyAllWindows()

