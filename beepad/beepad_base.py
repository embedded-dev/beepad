import board
import busio
import displayio
import digitalio
import rotaryio
import keypad
import usb_hid
import neopixel

from adafruit_displayio_sh1106 import SH1106

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_base import KeyboardLayoutBase
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.Mouse import Mouse

from adafruit_debouncer import Button

from .constants import KEYS


from .constants import OLED_HEIGHT, OLED_WIDTH, PIXEL_ORDER, PIXEL_BRIGHTNESS, PIXEL_NUM

class BeePadBase:

    def __init__(self):

        self._mouse = None
        self._consumer_control = None

        self._init_display()
        self._init_keypad()
        self._init_encoder()
        self._init_usb_hid()
        self._init_neopixel()

    def _init_display(self):
        displayio.release_displays()
        spi = busio.SPI(board.SCK, board.MOSI)
        display_bus = displayio.FourWire(spi,
                                         command=board.OLED_DC,
                                         chip_select=board.OLED_CS,
                                         reset=board.OLED_RESET,
                                         baudrate=1000000)
        self.display = SH1106(display_bus, width=OLED_WIDTH, height=OLED_HEIGHT)
        self.display.auto_refresh = False

    def _init_keypad(self):
        # Initialize the key with values 'board.KEYn' for 1 <= n <= 12
        key_pins = [getattr(board, "KEY%d" % (key + 1)) for key in range(0, KEYS)]
        self.keys = keypad.Keys(key_pins, value_when_pressed=False, pull=True)

    def _init_encoder(self):
        self.encoder = rotaryio.IncrementalEncoder(board.ROTB, board.ROTA)
        self.encoder.position = 0
        self._encoder_switch = digitalio.DigitalInOut(board.ENCODER_SWITCH)
        self._encoder_switch.switch_to_input(pull=digitalio.Pull.UP)
        self._debounced_switch = Button(self._encoder_switch)
        self._debounced_switch.update()

    def _init_usb_hid(self):
        self.keyboard = Keyboard(usb_hid.devices)
        self.keyboard_layout = KeyboardLayoutUS(self.keyboard)
        self._consumer_control = ConsumerControl(usb_hid.devices)

    def _init_neopixel(self):
        self.pixels = neopixel.NeoPixel(board.NEOPIXEL, PIXEL_NUM,
                                        brightness=PIXEL_BRIGHTNESS,
                                        auto_write=False,
                                        pixel_order=PIXEL_ORDER)

    @property
    def encoder_switch_debounced(self) -> Button:
        return self._debounced_switch

    @property
    def mouse(self) -> adafruit_hid.mouse.Mouse:
        if not self._mouse:
            self._mouse = Mouse(usb_hid.devices)
        return self._mouse

    @property
    def consumer_control(self) -> adafruit_hid.consumer_control.ConsumerControl:
        if not self._consumer_control:
            self._consumer_control = ConsumerControl(usb_hid.devices)
        return self._consumer_control