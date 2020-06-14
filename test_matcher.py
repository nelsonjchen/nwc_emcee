# content of test_sample.py
import cv2

from scene import TitleScreen, MarioGameScreen, RadRacerGameScreen, TetrisGameScreen


def hsv_image(path):
    img = cv2.imread(path)

    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# noinspection DuplicatedCode
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
    assert not scene.match(hsv_image('samples/snap_9632.png'))
    assert not scene.match(hsv_image('samples/snap_10142.png'))
    assert not scene.match(hsv_image('samples/snap_10452.png'))
    assert not scene.match(hsv_image('samples/snap_10683.png'))
    assert not scene.match(hsv_image('samples/snap_11118.png'))
    assert not scene.match(hsv_image('samples/snap_12417.png'))
    assert not scene.match(hsv_image('samples/snap_13042.png'))
    assert not scene.match(hsv_image('samples/snap_14042.png'))
    assert not scene.match(hsv_image('samples/snap_17935.png'))
    assert not scene.match(hsv_image('samples/snap_19519.png'))
    assert not scene.match(hsv_image('samples/snap_20038.png'))
    assert not scene.match(hsv_image('samples/snap_24277.png'))
    assert not scene.match(hsv_image('samples/snap_24356.png'))
    assert not scene.match(hsv_image('samples/snap_24523.png'))


# noinspection DuplicatedCode
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
    assert not scene.match(hsv_image('samples/snap_9632.png'))
    assert not scene.match(hsv_image('samples/snap_10142.png'))
    assert not scene.match(hsv_image('samples/snap_10452.png'))
    assert not scene.match(hsv_image('samples/snap_10683.png'))
    assert not scene.match(hsv_image('samples/snap_11118.png'))
    assert not scene.match(hsv_image('samples/snap_12417.png'))
    assert not scene.match(hsv_image('samples/snap_13042.png'))
    assert not scene.match(hsv_image('samples/snap_14042.png'))
    assert not scene.match(hsv_image('samples/snap_17935.png'))
    assert not scene.match(hsv_image('samples/snap_19519.png'))
    assert not scene.match(hsv_image('samples/snap_20038.png'))
    assert not scene.match(hsv_image('samples/snap_24277.png'))
    assert not scene.match(hsv_image('samples/snap_24356.png'))
    assert not scene.match(hsv_image('samples/snap_24523.png'))


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


def test_match_radracer():
    scene = RadRacerGameScreen()

    assert not scene.match(hsv_image('samples/snap_120.png'))
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
    assert not scene.match(hsv_image('samples/snap_9632.png'))
    # This isn't a game mode oddly
    assert not scene.match(hsv_image('samples/snap_10142.png'))
    assert scene.match(hsv_image('samples/snap_10452.png'))
    assert scene.match(hsv_image('samples/snap_10683.png'))
    assert scene.match(hsv_image('samples/snap_11118.png'))
    assert scene.match(hsv_image('samples/snap_12417.png'))
    assert scene.match(hsv_image('samples/snap_13042.png'))
    assert scene.match(hsv_image('samples/snap_14042.png'))
    assert scene.match(hsv_image('samples/snap_17935.png'))
    assert not scene.match(hsv_image('samples/snap_19519.png'))
    assert not scene.match(hsv_image('samples/snap_20038.png'))
    assert not scene.match(hsv_image('samples/snap_24277.png'))
    assert not scene.match(hsv_image('samples/snap_24356.png'))
    assert not scene.match(hsv_image('samples/snap_24523.png'))


def test_match_radracer_score():
    scene = RadRacerGameScreen()

    # assert scene.score(hsv_image('samples/snap_10142.png')) == 0
    assert scene.score(hsv_image('samples/snap_10452.png')) == 11
    assert scene.score(hsv_image('samples/snap_10683.png')) == 70
    assert scene.score(hsv_image('samples/snap_11118.png')) == 332
    assert scene.score(hsv_image('samples/snap_12417.png')) == 900
    assert scene.score(hsv_image('samples/snap_13042.png')) == 1406
    assert scene.score(hsv_image('samples/snap_14042.png')) == 2349
    assert scene.score(hsv_image('samples/snap_17935.png')) == 5649


def test_match_tetris():
    scene = TetrisGameScreen()

    assert not scene.match(hsv_image('samples/snap_120.png'))
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
    assert not scene.match(hsv_image('samples/snap_9632.png'))
    # This isn't a game mode oddly
    assert not scene.match(hsv_image('samples/snap_10142.png'))
    assert not scene.match(hsv_image('samples/snap_10452.png'))
    assert not scene.match(hsv_image('samples/snap_10683.png'))
    assert not scene.match(hsv_image('samples/snap_11118.png'))
    assert not scene.match(hsv_image('samples/snap_12417.png'))
    assert not scene.match(hsv_image('samples/snap_13042.png'))
    assert not scene.match(hsv_image('samples/snap_14042.png'))
    assert not scene.match(hsv_image('samples/snap_17935.png'))
    assert not scene.match(hsv_image('samples/snap_19519.png'))
    assert scene.match(hsv_image('samples/snap_20038.png'))
    assert not scene.match(hsv_image('samples/snap_24277.png'))
    assert not scene.match(hsv_image('samples/snap_24356.png'))
    assert not scene.match(hsv_image('samples/snap_24523.png'))
    assert scene.match(hsv_image('samples/snap_44806.png'))
    assert scene.match(hsv_image('samples/snap_44930.png'))
    assert scene.match(hsv_image('samples/snap_45095.png'))
    assert scene.match(hsv_image('samples/snap_45307.png'))
    assert scene.match(hsv_image('samples/snap_46104.png'))
    assert scene.match(hsv_image('samples/snap_47805.png'))
    assert scene.match(hsv_image('samples/snap_48736.png'))
    assert scene.match(hsv_image('samples/snap_50100.png'))
    assert scene.match(hsv_image('samples/snap_50132.png'))
    assert scene.match(hsv_image('samples/snap_50133.png'))
    assert scene.match(hsv_image('samples/snap_50212.png'))

def test_match_tetris_score():
    scene = TetrisGameScreen()

    assert scene.score(hsv_image('samples/snap_20038.png')) == 11
    assert scene.score(hsv_image('samples/snap_44806.png')) == 12
    assert scene.score(hsv_image('samples/snap_44930.png')) == 23
    assert scene.score(hsv_image('samples/snap_45095.png')) == 33
    assert scene.score(hsv_image('samples/snap_45307.png')) == 94
    assert scene.score(hsv_image('samples/snap_46104.png')) == 190
    assert scene.score(hsv_image('samples/snap_47805.png')) == 532
    assert scene.score(hsv_image('samples/snap_48736.png')) == 764
    assert scene.score(hsv_image('samples/snap_50100.png')) == 1593
    assert scene.score(hsv_image('samples/snap_50132.png')) == 1593
    assert scene.score(hsv_image('samples/snap_50133.png')) == 1593
    assert scene.score(hsv_image('samples/snap_50212.png')) == 1593