import math
import time
import cv2
import mediapipe as mp

from utils import get_coord


class HandDetector:

    def __init__(self, *args, **kwargs):

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(*args, **kwargs)
        self.mp_draw = mp.solutions.drawing_utils

    def _instance_img(self, img):
        self.results = self.hands.process(img)

    def get_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self._instance_img(img_rgb)
        if self.results.multi_hand_landmarks:
            for handimg in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, handimg, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_lm_positions(self, img, hand_number=0, draw=True):
        lm_list = []
        if self.results.multi_hand_landmarks:
            hands_detected = self.results.multi_hand_landmarks[hand_number]
            for id_, lm in enumerate(hands_detected.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id_, cx, cy])
            return lm_list

    @staticmethod
    def get_finger_up(lm, finger_id, finger_length):
        starting_index = finger_id * 4 + 1
        end_index = finger_id * 4 + 4

        x1, y1 = get_coord(lm, id_=starting_index)
        x2, y2 = get_coord(lm, id_=end_index)
        length = math.hypot(x2 - x1, y2 - y1)
        if length > finger_length:
            return x1, y1, True
        else:
            return x1, y1, False


"""def run_capture():
    ctime = 0
    ptime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.find_hands(img=img)
        lm_list = detector.find_position(img)
        if lm_list:
            print(lm_list[0])
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow('image', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    run_capture()
"""
