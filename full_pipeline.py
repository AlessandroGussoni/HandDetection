import cv2

from config import Config
from entities.breakpoints.mouse import MouseBreakPoint
from entities.breakpoints.volume import VolumeBreakPoint
from entities.detection import HandDetector
from entities.sound_system import AudioSystem
from pipelines.mouse import mouse_control_pipeline
from pipelines.volume import volume_control_pipeline


def main_pipeline(config):
    audio_stop_frames = 0
    mouse_stop_frames = 0
    # steup hand detection
    detector = HandDetector()
    # steup audio system
    audios = AudioSystem()
    audios.get_system_volume()
    min_volume, max_volume = audios.get_volume_range()
    audio_run, mouse_run, main_run = True, True, True
    # bp instances
    vbp = VolumeBreakPoint(config, audio_stop_frames)
    mbp = MouseBreakPoint(config, mouse_stop_frames)
    # video capture
    cap = cv2.VideoCapture(0)

    while main_run:
        success, img = cap.read()
        img = detector.get_hands(img=img)
        lm = detector.find_lm_positions(img, draw=False)
        audio_run = vbp.return_run(lm, audio_run)
        print(audio_run)
        if audio_run:
            img, audio_run = volume_control_pipeline(config,
                                                     img,
                                                     lm,
                                                     audios,
                                                     min_volume, max_volume,
                                                     vbp,
                                                     audio_run)
        """mouse_run = mbp.return_run(lm, mouse_run)
        if mouse_run:
            mouse_run = mouse_control_pipeline(config,
                                               img,
                                               detector,
                                               mbp,
                                               mouse_run
                                               )"""
        cv2.imshow('img', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    config = Config()
    main_pipeline(config)
