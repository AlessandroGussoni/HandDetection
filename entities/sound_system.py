from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class AudioSystem:

    def __init__(self):
        pass

    def _instance_volume(self, interface, endpoint):
        self.volume = cast(interface, endpoint)

    def get_system_volume(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self._instance_volume(interface, POINTER(IAudioEndpointVolume))

    def get_volume_range(self):
        vol_range = self.volume.GetVolumeRange()
        return vol_range[0], vol_range[1]
