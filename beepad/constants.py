import neopixel
from micropython import const

KEYS = const(3 * 4)

PIXEL_NUM = const(12)
PIXEL_ORDER = neopixel.GRB
PIXEL_BRIGHTNESS = 0.25

OLED_WIDTH = const(128)
OLED_HEIGHT = const(64)
OLED_BORDER = const(1)
