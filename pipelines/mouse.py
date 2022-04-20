import cv2
import pyautogui


def mouse_control_pipeline(config,
                           img,
                           detector,
                           bp_instance,
                           run):
    img = cv2.resize(img, [config.screen_width, config.screen_height])
    img = detector.get_hands(img=img)
    lm = detector.find_lm_positions(img)
    if lm:
        x1, y1, flag1 = detector.get_finger_up(lm, 1, config.fingers['1'])
        x2, y2, flag2 = detector.get_finger_up(lm, 2, config.fingers['2'])

        if flag1 and not flag2:
            pyautogui.moveTo(config.screen_width - int(x1), int(y1))
            print(config.screen_width - int(x1), x1, y1)
            print('Routing ...')

        elif flag1 and flag2:
            pyautogui.mouseDown()

        elif not flag1 and flag2:
            pyautogui.mouseUp()

    run = bp_instance.return_run(lm, run)

    return run
