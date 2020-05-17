import time

import numpy as np
import cv2

from scene import TitleScreen

cap = cv2.VideoCapture('D:\\Nintendo World Championships 1990 (U) [!].avi')
# cap = cv2.VideoCapture(0)

frame_number = 0

ts = TitleScreen()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ts.match(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)):
        title_match = "TITLE!"
    else:
        title_match = "NOT TITLE!"

    # Display the resulting frame
    cv2.putText(frame, title_match, (50,50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255,0,255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    frame_number += 1

    if cv2.waitKey(1) & 0xFF == ord('s'):
        status = cv2.imwrite(f'samples/snap_{frame_number}.png', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()