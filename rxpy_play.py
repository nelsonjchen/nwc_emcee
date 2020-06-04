import asyncio

import cv2
import rx
from rx import operators as ops

# cap = cv2.VideoCapture(0)
from rx.scheduler import ImmediateScheduler


from scene import TitleScreen

cap = cv2.VideoCapture('D:\\Nintendo World Championships 1990 (U) [!].avi')
# cap = cv2.VideoCapture(0)

loop = asyncio.get_event_loop()

def capture_frame(_):
    ret, frame = cap.read()
    return frame

def show(frame):
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

async def show_coroutine(image):
    cv2.imshow('res', image)
    return cv2.waitKey(1) & 0xff

def show(image):
    """
    """
    future = asyncio.run_coroutine_threadsafe(show_coroutine(image), loop)
    key = future.result()
    if key == ord('q'):
        loop.stop()

clock_source = rx.interval(1/60)

composed = clock_source.pipe(
    ops.map(lambda _: cap.read()),
    ops.filter(lambda data: data[0]),
    ops.map(lambda data: data[1]),
    ops.map(lambda etc_frame: cv2.resize(etc_frame,(256,224))),
    # ops.map(match_title_screen)
)
composed.subscribe(show)

loop.run_forever()
cap.release()
loop.close()