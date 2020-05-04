import time

import numpy as np
import cv2

cap = cv2.VideoCapture('D:\\Nintendo World Championships 1990 (U) [!].avi')
# cap = cv2.VideoCapture(0)

frame_number = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    frame_number += 1

    if cv2.waitKey(1) & 0xFF == ord('s'):
        status = cv2.imwrite(f'samples/snap_{frame_number}.png', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()