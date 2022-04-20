import cv2


def draw_sound_control_landmarks(img, p1, p2, c1):
    cv2.circle(img, [p1[0], p1[1]], 15, (255, 0, 255), cv2.FILLED)
    cv2.circle(img, [p2[0], p2[1]], 15, (255, 0, 255), cv2.FILLED)
    cv2.line(img, [p1[0], p1[1]], [p2[0], p2[1]], (255, 0, 255), 3)
    cv2.circle(img, [c1[0], c1[1]], 15, (255, 0, 255), cv2.FILLED)
