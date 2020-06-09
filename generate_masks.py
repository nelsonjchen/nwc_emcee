# lower mask (0-10)
import cv2
import numpy as np


# Generate


def blue_mask():
    img = cv2.imread('samples/snap_120.png')

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([120, 255, 255])
    blue_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

    cv2.imwrite('masks/title_blue_raw.png', blue_mask, [cv2.IMWRITE_PNG_BILEVEL, 1])


def mario_mask():
    mask_images = [
        "snap_762.png",
        "snap_857.png",
        "snap_1079.png",
        "snap_2078.png",
        "snap_2387.png",
        "snap_2576.png",
        "snap_2791.png",
        "snap_2969.png",
        "snap_3177.png",
        "snap_3267.png",
        "snap_3490.png",
        "snap_3558.png",
        "snap_3644.png",
        "snap_3898.png",
        "snap_4361.png",
        "snap_4633.png",
        "snap_4835.png",
        "snap_5091.png",
        "snap_5508.png",
        "snap_6046.png",
        "snap_6155.png",
        "snap_6244.png",
    ]
    samples = [
        cv2.imread(f"samples/{mask_image}") for mask_image in mask_images
    ]

    samples_hsvs = [
        cv2.cvtColor(sample, cv2.COLOR_BGR2HSV) for sample in samples
    ]

    lower_white = np.array([0, 0, 250])
    upper_white = np.array([10, 10, 255])

    masked_images = [
        cv2.inRange(sample_hsv, lower_white, upper_white) for sample_hsv in samples_hsvs
    ]

    and_mask_image = masked_images[0]
    for rest_sample_hsv in masked_images[1:]:
        and_mask_image = and_mask_image & rest_sample_hsv

    cv2.imwrite('masks/title_mario_raw.png', and_mask_image, [cv2.IMWRITE_PNG_BILEVEL, 1])


blue_mask()

mario_mask()
