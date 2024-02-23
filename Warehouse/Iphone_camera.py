import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):  # wait for 's' key to save
        cv2.imwrite("snapshot.jpg", frame)

cap.release()
cv2.destroyAllWindows()
