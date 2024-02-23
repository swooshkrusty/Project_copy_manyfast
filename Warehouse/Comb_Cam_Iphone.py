import cv2
from pyzbar.pyzbar import decode
import time


# Function to add a color tint to the frame
def add_color_tint(frame, color):
    """
    Adds a color tint to the frame.
    :param frame: The original image.
    :param color: A tuple of BGR values to add as a tint.
    :return: The color-tinted image.
    """
    return cv2.addWeighted(frame, 0.9, color, 0.1, 0)


# Replace the below URL with the streaming URL from your iPhone app.
stream_url = "http://YOUR_IPHONE_IP:PORT/video"
cap = cv2.VideoCapture(stream_url)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

used_codes = []

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Decode any barcodes in the frame
    for code in decode(frame):
        code_data = code.data.decode("utf-8")
        if code_data not in used_codes:
            print("Approved. You can enter!")
            print(code_data)
            used_codes.append(code_data)
            frame = add_color_tint(frame, (0, 255, 0))
            time.sleep(5)
        else:
            print("Sorry, this code has been already used!")
            frame = add_color_tint(frame, (0, 0, 255))
            time.sleep(5)

    # Display the resulting frame
    cv2.imshow("Testing-code-scan", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
