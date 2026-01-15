from handTracking import HandTracker
import cv2
import numpy as np

tracker = HandTracker()
canvas = None

while True:
    hands, frame = tracker.get_frame()
    if canvas is None:
        canvas = np.zeros_like(frame)

    if hands:
        hand = hands[0]

    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow("Virtual Paint", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

tracker.release()
