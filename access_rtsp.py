import cv2

cap = cv2.VideoCapture("rtsp://localhost:8554/stream1")

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cap.release()