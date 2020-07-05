import time
from collections import deque
from queue import Queue
from typing import List

import cv2

from scene import TitleScreen, Screen, MarioGameScreen, RadRacerGameScreen, ScoreScreen, TetrisGameScreen

import numpy as np

import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
if gpus:
  try:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
  except RuntimeError as e:
    print(e)


from tensorflow import keras

model = keras.models.load_model('class_ml')

# 256x224
# cap = cv2.VideoCapture('D:\\alt_Nintendo World Championships 1990 (U) [!]_1.avi')

# Random youtube
# cap = cv2.VideoCapture('D:\\random_youtube_nwc.mp4')
cap = cv2.VideoCapture('D:\\vhsmillions.mp4')

random_yt = True
# webcam = False

# 480 x 640
# cap = cv2.VideoCapture(0)
webcam = True

frame_number = 0

screens: List[Screen] = [
    TitleScreen(),
    MarioGameScreen(),
    RadRacerGameScreen(),
    TetrisGameScreen(),
]

classes = [
    'ready',
    'mario_score',
    'radracer_score',
    'tetris_score',
    'final_score',
]


def array_to_class(prediction: np.ndarray):
    return classes[int(np.argmax(prediction))]

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame_number += 1

    if frame_number % 2 == 0:
        continue

    # if random_yt:
    #     frame = frame[10: 345, 30: 620]

    frame = cv2.resize(frame, (256, 224))

    # title_match = "Unknown"

    #
    # for screen in screens:
    #     hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #     if screen.match(hsv_image):
    #         title_match = screen.__class__.__name__
    #         if isinstance(screen, ScoreScreen):
    #             score = screen.score(hsv_image)
    #             title_match = f"{score}-{screen.__class__.__name__}"
    frame_cup = np.expand_dims(frame, axis=0)
    title_match = array_to_class(model.predict(frame_cup))

    # Display the resulting frame
    cv2.putText(frame, title_match, (0, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        status = cv2.imwrite(f'samples/snap_{frame_number}.png', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
