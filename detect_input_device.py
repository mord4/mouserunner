from evdev import InputDevice, list_devices, ecodes as e
from typing import Callable


def _caps(path: str):
    return dict(InputDevice(path).capabilities())


def _is_mouse(caps: dict):
    return (
        e.EV_REL in caps
        and e.REL_X in caps[e.EV_REL]
        and e.REL_Y in caps[e.EV_REL]
    )


def _is_touchpad(caps: dict):
    return (
        e.EV_KEY in caps
        and e.BTN_TOUCH in caps[e.EV_KEY]
    )


def _find_device(predicate: Callable[[dict], bool]):
    for path in list_devices():
        caps = _caps(path)
        if predicate(caps):
            print("detect:", path)
            return InputDevice(path)
    print("detect: None")
    return None


def detect_mouse():
    return _find_device(_is_mouse)



def detect_touchpad():
    return _find_device(_is_touchpad)

