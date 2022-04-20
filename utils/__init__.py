import time
import cv2


def compute_fps(ptime):
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    return int(fps), ctime


def get_coord(lm, id_):
    return lm[id_][1], lm[id_][2]


def add_text(img, text, *args, **kwargs):
    cv2.putText(img, text, *args, **kwargs)
    return img
