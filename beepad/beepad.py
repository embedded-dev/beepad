from beepad.beepad_base import BeePadBase
from beepad.keymap import Keymap

from .constants import PIXEL_NUM
from .colours import colorwheel

from .display_layout import DisplayLayout

class BeePad(BeePadBase):

    def __init__(self, keymaps, assigned_colors=True, floating_colors=False) -> None:

        super().__init__()
        self._assigned_colors = assigned_colors
        self._floating_colors = floating_colors
        self.tick_count = 0

        self._keymaps = []
        for keymap in keymaps:
            self._keymaps.append(Keymap(**keymap))
        loaded = Keymap.load_all('macros')
        if len(loaded) > 0:
            self._keymaps.extend(loaded)
        self._keymaps.sort(key=lambda m:m.priority, reverse=True)

        self.layout = DisplayLayout(self.display)
        self._current_screen: int = 0
        self.layout.show_keymap(self._keymaps[0])

        self.show_key_colors()

    def show_key_colors(self) -> None:
        slowdown = 10
        for i in range(PIXEL_NUM):
            action = self.current_keymap.actions[i]
            if self._assigned_colors and action.color:
                    self.pixels[i] = action.color
            elif self._floating_colors:
                color_index = (i * 256 // PIXEL_NUM) + (self.tick_count // slowdown % 256)
                self.pixels[i] = colorwheel(color_index & 255)
            else:
                self.pixels[i] = 0x000000
        self.pixels.show()

    @property
    def current_screen(self) -> int:
        return self._current_screen

    @property
    def current_keymap(self) -> Keymap:
        return self._keymaps[self.current_screen]

    @current_screen.setter
    def current_screen(self, val: int) -> None:
        if val != self._current_screen:
            self._current_screen = val
            self.layout.show_keymap(self._keymaps[val])
            self.show_key_colors()

    def buzz(self) -> None:
        self.tick_count += 1
        self.current_screen = self.encoder.position % len(self._keymaps)

        action = None
        self.encoder_switch_debounced.update()
        if self.encoder_switch_debounced.pressed:
            action = self.current_keymap.actions[12]
            action.pressed(self)
        else:
            event = self.keys.events.get()
            if event:
                action = self.current_keymap.actions[event.key_number]
                if event.pressed:
                    action.press(self)
                else:
                    action.release(self)

        self.show_key_colors()
        self.layout.refresh()

