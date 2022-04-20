import math

from entities.breakpoints import IAbstractBreakpoint
from utils import get_coord


class MouseBreakPoint(IAbstractBreakpoint):

    def __init__(self,
                 config,
                 counter):
        self.config = config
        self.counter = counter

    def return_run(self, lm, state):
        if lm:
            x1, y1 = get_coord(lm, id_=4)
            stop_x, stop_y = get_coord(lm, id_=16)
            stop_length = math.hypot(stop_x - x1, stop_y - y1)
            if (stop_length < self.config.stop_length) and ():
                self.counter += 1
            else:
                self.counter = 0

            if self.counter >= self.config.audio['stop_frames']:
                return not state
            else:
                return state
        else:
            return state