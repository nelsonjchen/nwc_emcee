from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np


@dataclass
class Matcher():
    mask_path: Path
    origin_x: int
    origin_y: int
    crop_width: int
    crop_height: int
    threshold_val = 127
    threshold_percentage: int

    def __post_init__(self):
        if not self.mask_path.exists():
            raise FileNotFoundError
        image = cv2.imread(
            str(self.mask_path)
        )[self.origin_y: self.origin_y + self.crop_height,
                     self.origin_x: self.origin_x + self.crop_width]
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, self.mask_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    def match(self, grayscale_frame_image) -> bool:
        cropped_grayscale_frame_image = grayscale_frame_image[
                                        self.origin_y: self.origin_y + self.crop_height,
                                        self.origin_x: self.origin_x + self.crop_width
                                        ]
        ret, threshold_cropped_grayscale_frame_image = cv2.threshold(
            cropped_grayscale_frame_image,
            self.threshold_val,
            255,
            cv2.THRESH_BINARY)

        count = np.count_nonzero(
            np.logical_and(
                self.mask_image,
                threshold_cropped_grayscale_frame_image
            )
        )
        percentage = (
                             100 * count
                     ) // self.mask_image.size
        return percentage < self.threshold_percentage


TitleMatcher = Matcher(
    Path('masks/title.png'),
    origin_x=0,
    origin_y=0,
    crop_width=256,
    crop_height=224,
    threshold_percentage=5
)
