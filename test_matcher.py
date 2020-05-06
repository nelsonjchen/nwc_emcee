# content of test_sample.py
import cv2

from matcher import TitleMatcher


def grayscale_image(path):
    sample_image = cv2.imread(path)
    return cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)


def test_match():
    assert TitleMatcher.match(grayscale_image('samples/snap_120.png'))
    assert not TitleMatcher.match(grayscale_image('samples/snap_459.png'))
    assert not TitleMatcher.match(grayscale_image('samples/snap_5508.png'))
