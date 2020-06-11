import cv2 as cv

# capture
cam = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("Saved.avi", fourcc, 20.0, (640, 480))
while True:
    ret, frame = cam.read()
    cv.write(frame)
    
    cv.imshow("Camera", frame)
    if cv.waitkey(1) & 0xFF == ord("q"):
        break

cam.release()
cv.destroyAllWindows()

