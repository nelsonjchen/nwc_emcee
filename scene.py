import cv2
import numpy as np
from numpy.core.multiarray import ndarray


# TODO: Figure out API
class TitleScreen:
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
