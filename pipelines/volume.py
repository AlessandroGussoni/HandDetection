import math
import time

import cv2
import numpy as np

from utils import get_coord
from utils.drawing import draw_sound_control_landmarks


def volume_control_pipeline(config,
                            img,
                            lm,
                            audios,
                            min_volume, max_volume,
                            bp_instance,
                            run):
    if lm:
        x1, y1 = get_coord(lm, id_=4)
        x2, y2 = get_coord(lm, id_=8)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        draw_sound_control_landmarks(img, [x1, y1], [x2, y2], [cx, cy])

        length = math.hypot(x2 - x1, y2 - y1)

        if length < config.min_length:
            cv2.circle(img, [cx, cy], 15, (0, 255, 0), cv2.FILLED)

        vol = np.interp(length, [config.min_length, config.max_length], [min_volume, max_volume])
        audios.volume.SetMasterVolumeLevel(vol, None)
        run = bp_instance.return_run(lm, run)

    return img, run