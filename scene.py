import cv2
import numpy as np
from numpy.core.multiarray import ndarray


class Screen:
    def match(self, image_hsv: ndarray) -> bool:
        raise NotImplementedError


class TitleScreen(Screen):
    def __init__(self):
        raw_mask = cv2.imread('masks/title_blue.png')
        raw_greyscale_mask = cv2.cvtColor(raw_mask, cv2.COLOR_BGR2GRAY)
        _, self.mask = cv2.threshold(raw_greyscale_mask, 10, 255, cv2.THRESH_BINARY)

    def match(self, image_hsv: ndarray) -> bool:
        lower_bound = np.array([100, 50, 50])
        upper_bound = np.array([120, 255, 255])

        blue_mask = cv2.inRange(image_hsv, lower_bound, upper_bound)
        xor_mask = cv2.bitwise_xor(self.mask, blue_mask)

        return np.count_nonzero(xor_mask) < 500


class MarioGameScreen(Screen):
    def __init__(self):
        raw_mask = cv2.imread('masks/title_mario_raw.png')
        raw_greyscale_mask = cv2.cvtColor(raw_mask, cv2.COLOR_BGR2GRAY)
        # Crop mask to just the top
        _, self.mask = cv2.threshold(raw_greyscale_mask, 10, 255, cv2.THRESH_BINARY)
        self.mask = self.mask[0:16, 0:256]

    def match(self, image_hsv: ndarray) -> bool:
        # Crop to just top
        cropped_image_hsv = image_hsv[0:16, 0:256]
        lower_white = np.array([0, 0, 250])
        upper_bound = np.array([10, 10, 255])

        white_mask = cv2.inRange(cropped_image_hsv, lower_white, upper_bound)
        xor_mask = cv2.bitwise_xor(self.mask, white_mask)

        return np.count_nonzero(xor_mask) < 500
