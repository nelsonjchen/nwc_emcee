# content of test_sample.py
import cv2

from scene import TitleScreen, MarioGameScreen


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


def test_match_mario():
    scene = MarioGameScreen()

    assert not scene.match(hsv_image('samples/snap_120.png'))
    assert not scene.match(hsv_image('samples/snap_459.png'))
    assert scene.match(hsv_image('samples/snap_762.png'))
    assert scene.match(hsv_image('samples/snap_857.png'))
    assert scene.match(hsv_image('samples/snap_1079.png'))
    assert scene.match(hsv_image('samples/snap_2078.png'))
    assert scene.match(hsv_image('samples/snap_2387.png'))
    assert scene.match(hsv_image('samples/snap_2576.png'))
    assert scene.match(hsv_image('samples/snap_2791.png'))
    assert scene.match(hsv_image('samples/snap_2969.png'))
    assert scene.match(hsv_image('samples/snap_3177.png'))
    assert scene.match(hsv_image('samples/snap_3267.png'))
    assert scene.match(hsv_image('samples/snap_3490.png'))
    assert scene.match(hsv_image('samples/snap_3558.png'))
    assert scene.match(hsv_image('samples/snap_3644.png'))
    assert scene.match(hsv_image('samples/snap_3898.png'))
    assert scene.match(hsv_image('samples/snap_4361.png'))
    assert scene.match(hsv_image('samples/snap_4633.png'))
    assert scene.match(hsv_image('samples/snap_4835.png'))
    assert scene.match(hsv_image('samples/snap_5091.png'))
    assert scene.match(hsv_image('samples/snap_5508.png'))
    assert scene.match(hsv_image('samples/snap_6046.png'))
    assert scene.match(hsv_image('samples/snap_6155.png'))
    assert scene.match(hsv_image('samples/snap_6244.png'))


def test_match_mario_score():
    scene = MarioGameScreen()
    assert scene.score(hsv_image('samples/snap_762.png')) == 0
    assert scene.score(hsv_image('samples/snap_857.png')) == 0
    assert scene.score(hsv_image('samples/snap_1079.png')) == 0
    assert scene.score(hsv_image('samples/snap_2078.png')) == 300
    assert scene.score(hsv_image('samples/snap_2387.png')) == 300
    assert scene.score(hsv_image('samples/snap_2576.png')) == 600
    assert scene.score(hsv_image('samples/snap_2791.png')) == 1800
    assert scene.score(hsv_image('samples/snap_2969.png')) == 1800
    assert scene.score(hsv_image('samples/snap_3177.png')) == 1900
    assert scene.score(hsv_image('samples/snap_3267.png')) == 2200
    assert scene.score(hsv_image('samples/snap_3490.png')) == 3000
    assert scene.score(hsv_image('samples/snap_3558.png')) == 5200
    assert scene.score(hsv_image('samples/snap_3644.png')) == 5600
    assert scene.score(hsv_image('samples/snap_3898.png')) == 6000
    assert scene.score(hsv_image('samples/snap_4361.png')) == 6300
    assert scene.score(hsv_image('samples/snap_4633.png')) == 6300
    assert scene.score(hsv_image('samples/snap_4835.png')) == 16550
    assert scene.score(hsv_image('samples/snap_5091.png')) == 27550
    assert scene.score(hsv_image('samples/snap_5508.png')) == 27550
    assert scene.score(hsv_image('samples/snap_6046.png')) == 28150
    assert scene.score(hsv_image('samples/snap_6155.png')) == 28550
    assert scene.score(hsv_image('samples/snap_6244.png')) == 28650
