import terminalio
import displayio
from adafruit_display_text import label

from .constants import OLED_HEIGHT, OLED_WIDTH, OLED_BORDER, KEYS

class DisplayLayout:

    def __init__(self, display) -> None:
        self._display = display

        self._key_visual = displayio.Group()
        self._display.root_group = self._key_visual

        self._draw_background()
        self._draw_labels()

    def _draw_background(self) -> None:
        """Draw the background"""
        color_bitmap = displayio.Bitmap(OLED_WIDTH, OLED_HEIGHT, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        self._key_visual.append(bg_sprite)

        # Draw a smaller inner rectangle, black
        inner_bitmap = displayio.Bitmap(OLED_WIDTH - OLED_BORDER * 2 - 2,
                                        OLED_HEIGHT - OLED_BORDER * 2, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette,
                                          x=OLED_BORDER + 2, y=OLED_BORDER)
        self._key_visual.append(inner_sprite)

    def _draw_labels(self) -> None:
        self._name = label.Label(terminalio.FONT, text=" " * 6,
                                 color=0xFFFFFF, x=OLED_WIDTH // 2 - 10, y=10)
        self._key_visual.append(self._name)

        # create the text area to hold key descriptions
        self._key_labels = []

        for y in [20, 30, 40, 50]:
            for x in [10, 50, 90]:
                l = label.Label(terminalio.FONT, text=" " * 6, color=0xFFFFFF, x=x, y=y)
                self._key_visual.append(l)
                self._key_labels.append(l)

    def show_keymap(self, keymap) -> None:
        self._name.text = keymap.name
        for i in range(0, KEYS):
            self._key_labels[i].text = keymap.actions[i].name

    def refresh(self) -> None:
        self._display.refresh()

