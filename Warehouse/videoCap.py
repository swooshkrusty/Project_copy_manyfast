import cv2


def add_color_tint(frame, color):
    """
    Adds a color tint to the frame.

    :param frame: The original image.
    :param color: A tuple of BGR values to add as a tint.
    :return: The color-tinted image.
    """
    return cv2.addWeighted(frame, 0.9, color, 0.1, 0)


# This will use the default camera (usually the built-in camera if you're on a laptop)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    col_85 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow("frame", col_85)

    # Press 'q' on the keyboard to exit the loop
    if cv2.waitKey(1) == ord("q"):
        break


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
