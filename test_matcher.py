# content of test_sample.py
import cv2

from scene import TitleScreen


def hsv_image(path):
    img = cv2.imread(path)

    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def test_match():
    scene = TitleScreen()

    assert scene.match(hsv_image('samples/snap_120.png'))
    assert not scene.match(hsv_image('samples/snap_459.png'))
    assert not scene.match(hsv_image('samples/snap_762.png'))
    assert not scene.match(hsv_image('samples/snap_857.png'))
    assert not scene.match(hsv_image('samples/snap_1079.png'))
    assert not scene.match(hsv_image('samples/snap_2078.png'))
    assert not scene.match(hsv_image('samples/snap_2387.png'))
    assert not scene.match(hsv_image('samples/snap_2576.png'))
    assert not scene.match(hsv_image('samples/snap_2791.png'))
    assert not scene.match(hsv_image('samples/snap_2969.png'))
    assert not scene.match(hsv_image('samples/snap_3177.png'))
    assert not scene.match(hsv_image('samples/snap_3267.png'))
    assert not scene.match(hsv_image('samples/snap_3490.png'))
    assert not scene.match(hsv_image('samples/snap_3558.png'))
    assert not scene.match(hsv_image('samples/snap_3644.png'))
    assert not scene.match(hsv_image('samples/snap_3898.png'))
    assert not scene.match(hsv_image('samples/snap_4361.png'))
    assert not scene.match(hsv_image('samples/snap_4633.png'))
    assert not scene.match(hsv_image('samples/snap_4835.png'))
    assert not scene.match(hsv_image('samples/snap_5091.png'))
    assert not scene.match(hsv_image('samples/snap_5508.png'))
    assert not scene.match(hsv_image('samples/snap_6046.png'))
    assert not scene.match(hsv_image('samples/snap_6155.png'))
    assert not scene.match(hsv_image('samples/snap_6244.png'))
