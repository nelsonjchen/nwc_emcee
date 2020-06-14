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

        return np.count_nonzero(xor_mask) < 1500


class ScoreScreen(Screen):
    def score(self, image_hsv: ndarray) -> int:
        raise NotImplementedError


class MarioGameScreen(ScoreScreen):
    def __init__(self):
        raw_mask = cv2.imread('masks/title_mario_raw.png')
        raw_greyscale_mask = cv2.cvtColor(raw_mask, cv2.COLOR_BGR2GRAY)
        # Crop mask to just the top
        _, self.mask = cv2.threshold(raw_greyscale_mask, 10, 255, cv2.THRESH_BINARY)
        self.mask = self.mask[0:16, 0:256]

        palette_sheet = cv2.imread('sheets/mario.png')
        gray_palette_sheet = cv2.cvtColor(palette_sheet, cv2.COLOR_BGR2GRAY)

        _, masked = cv2.threshold(gray_palette_sheet, 10, 255, cv2.THRESH_BINARY)
        masked = cv2.bitwise_not(masked)
        palette_x = 128
        self.digit_images = []
        # Digit Images
        for digit in range(10):
            origin_palette_x = palette_x + 8 * digit
            self.digit_images.append(
                masked[0:7, origin_palette_x:origin_palette_x + 8]
            )

    def match(self, image_hsv: ndarray) -> bool:
        # Crop to just top
        cropped_image_hsv = image_hsv[0:16, 0:256]
        lower_white = np.array([0, 0, 250])
        upper_bound = np.array([10, 10, 255])

        white_mask = cv2.inRange(cropped_image_hsv, lower_white, upper_bound)
        xor_mask = cv2.bitwise_xor(self.mask, white_mask)

        return np.count_nonzero(xor_mask) < 100

    def score(self, image_hsv: ndarray) -> int:
        cropped_image_hsv = image_hsv[16:23, 24:72]
        lower_white = np.array([0, 0, 250])
        upper_bound = np.array([10, 10, 255])

        white_mask = cv2.inRange(cropped_image_hsv, lower_white, upper_bound)
        white_mask = cv2.bitwise_not(white_mask)
        score = 0

        for i in range(6):
            cropped_digit = white_mask[0:7, 0 + i * 8:8 + i * 8]
            detected_digit_and_diff = (None, 99999)
            for num, digit_image in enumerate(self.digit_images):
                xor_mask = cv2.bitwise_xor(cropped_digit, digit_image)
                count_nonzero = np.count_nonzero(xor_mask)

                if count_nonzero < detected_digit_and_diff[1]:
                    detected_digit_and_diff = (num, count_nonzero)
            detected_digit = detected_digit_and_diff[0]
            score += detected_digit * 100000 // (10 ** i)
        return score


class RadRacerGameScreen(ScoreScreen):
    def __init__(self):
        raw_mask = cv2.imread('masks/title_radracer_raw.png')
        raw_greyscale_mask = cv2.cvtColor(raw_mask, cv2.COLOR_BGR2GRAY)

        _, self.mask = cv2.threshold(raw_greyscale_mask, 10, 255, cv2.THRESH_BINARY)

        palette_sheet = cv2.imread('sheets/radracer_game.png')
        gray_palette_sheet = cv2.cvtColor(palette_sheet, cv2.COLOR_BGR2GRAY)

        _, masked = cv2.threshold(gray_palette_sheet, 250, 255, cv2.THRESH_BINARY)
        masked = cv2.bitwise_not(masked)
        # Digit Images
        palette_x = 0
        self.digit_images = []
        for digit in range(10):
            origin_palette_x = palette_x + 8 * digit
            self.digit_images.append(
                masked[25:32, origin_palette_x:origin_palette_x + 8]
            )

    def match(self, image_hsv: ndarray) -> bool:
        # Crop to just top
        cropped_image_hsv = image_hsv[168:224, 160:230]
        lower_bound = np.array([100, 200, 200])
        upper_bound = np.array([140, 255, 255])

        range_mask = cv2.inRange(cropped_image_hsv, lower_bound, upper_bound)
        xor_mask = cv2.bitwise_xor(self.mask, range_mask)

        return np.count_nonzero(xor_mask) < 500

    def score(self, image_hsv: ndarray) -> int:
        lower_bound = np.array([50, 100, 100])
        upper_bound = np.array([100, 255, 255])

        matcher_mask = cv2.inRange(image_hsv, lower_bound, upper_bound)
        matcher_mask = cv2.bitwise_not(matcher_mask)

        score = 0

        for i in range(5):
            cropped_digit = matcher_mask[203:210, 184 + i * 8:(184 + 8) + i * 8]
            detected_digit_and_diff = (None, 99999)
            for num, digit_image in enumerate(self.digit_images):
                xor_mask = cv2.bitwise_xor(cropped_digit, digit_image)
                count_nonzero = np.count_nonzero(xor_mask)

                if count_nonzero < detected_digit_and_diff[1]:
                    detected_digit_and_diff = (num, count_nonzero)
            detected_digit = detected_digit_and_diff[0]
            score += detected_digit * 10000 // (10 ** i)

        return score


class TetrisGameScreen(ScoreScreen):
    def __init__(self):
        raw_mask = cv2.imread('masks/game_tetris_statistic.png')
        raw_greyscale_mask = cv2.cvtColor(raw_mask, cv2.COLOR_BGR2GRAY)
        # Crop mask to just the top
        _, self.mask = cv2.threshold(raw_greyscale_mask, 10, 255, cv2.THRESH_BINARY)

        palette_sheet = cv2.imread('sheets/tetris_title.png')
        gray_palette_sheet = cv2.cvtColor(palette_sheet, cv2.COLOR_BGR2GRAY)

        _, masked = cv2.threshold(gray_palette_sheet, 100, 255, cv2.THRESH_BINARY)
        masked = cv2.bitwise_not(masked)
        palette_x = 0
        self.digit_images = []
        # Digit Images
        for digit in range(10):
            origin_palette_x = palette_x + 8 * digit
            self.digit_images.append(
                masked[0:7, origin_palette_x:origin_palette_x + 8]
            )

    def match(self, image_hsv: ndarray) -> bool:
        # Crop to just top
        cropped_image_hsv = image_hsv[64:71, 19:77]
        gray_match_img = cv2.cvtColor(cropped_image_hsv, cv2.COLOR_BGR2GRAY)
        _, thresh_match_img = cv2.threshold(gray_match_img, 10, 255, cv2.THRESH_BINARY)

        xor_mask = cv2.bitwise_xor(self.mask, thresh_match_img)

        return np.count_nonzero(xor_mask) < 100

    def score(self, image_hsv: ndarray) -> int:
        lower_white = np.array([0, 0, 250])
        upper_bound = np.array([10, 10, 255])

        white_mask = cv2.inRange(image_hsv, lower_white, upper_bound)
        white_mask = cv2.bitwise_not(white_mask)
        score = 0

        for i in range(6):
            cropped_digit = white_mask[56:63, 192+i*8:(192+8)+i*8]

            detected_digit_and_diff = (None, 99999)
            for num, digit_image in enumerate(self.digit_images):
                xor_mask = cv2.bitwise_xor(cropped_digit, digit_image)
                count_nonzero = np.count_nonzero(xor_mask)

                if count_nonzero < detected_digit_and_diff[1]:
                    detected_digit_and_diff = (num, count_nonzero)
            detected_digit = detected_digit_and_diff[0]
            score += detected_digit * 100000 // (10 ** i)
        return score
