__version__ = "1.0.0"
__author__ = "Твоё имя или ник"
__all__ = [
    "main",
    "detect_mouse",
    "detect_touchpad",
    "parse_args",
]

# Импорты верхнего уровня для удобства
from .mouserunner import mouserunner
from .detect_input_device import detect_mouse, detect_touchpad
from ._parse_arguments import parse_args