import os
from time import sleep

from .constants import KEYS


class Action:

    def __init__(self, name: str, color: int) -> None:
        self.name = name
        self.color = color

    def press(self, pad: 'BeePad') -> None:
        pass

    def release(self, pad: 'BeePad') -> None:
        pass


class NullAction(Action):

    def __init__(self) -> None:
        super(NullAction, self).__init__('', None)

    def press(self, pad: 'BeePad') -> None:
        pass

    def release(self, pad: 'BeePad') -> None:
        pass


class TypeAction(Action):

    def __init__(self, color: int, name: str, *sequence) -> None:
        super(TypeAction, self).__init__(name, color)
        self._sequence = sequence

    def press(self, pad: 'BeePad') -> None:
        # '_sequence' is an arbitrary-length list, each item is one of:
        #     + Positive integer: key pressed (e.g. Keycode.KEYPAD_MINUS)
        #     + Negative integer: key released (absolute value)
        #     + Float: delay in seconds (e.g. 0.10)
        #     + String: corresponding keys pressed & released (e.g. "git status")
        if self._sequence and len(self._sequence) != 0:
            for item in self._sequence:
                if isinstance(item, int):
                    if item >= 0:
                        pad.keyboard.press(item)
                    else:
                        pad.keyboard.release(-item)
                elif isinstance(item, float):
                    sleep(item)
                elif isinstance(item, str):
                    pad.keyboard_layout.write(item)

    def release(self, pad: 'BeePad') -> None:
        # Release any still-pressed keys, consumer codes, mouse buttons
        #
        # Keys and mouse buttons are individually released this way (rather
        # than release_all()) because pad supports multi-key rollover, e.g.
        # could have a meta key or right-mouse held down by one macro and
        # press/release keys/buttons with others. Navigate popups, etc.
        if self._sequence and len(self._sequence) != 0:
            for item in self._sequence:
                if isinstance(item, int) and item >= 0:
                    pad.keyboard.release(item)
        pad.consumer_control.release()


class MouseAction(Action):

    def __init__(self, color: int, name: str, x=None, y=None, buttons=None) -> None:
        super(TypeAction, self).__init__(name, color)
        self.x = x
        self.y = y
        self.buttons = buttons

    def press(self, pad: 'BeePad') -> None:
        if self.x or self.y:
            pad.mouse.move(self.x if self.x else 0,
                           self.y if self.y else 0,
                           0)
        if self.buttons:
            pad.mouse.click(self.buttons)

    def release(self, pad: 'BeePad') -> None:
        if self.buttons:
            pad.mouse.release(self.buttons)


class ConsumerControlAction(Action):

    def __init__(self, color: int, name: str, *codes) -> None:
        super(TypeAction, self).__init__(name, color)
        self._codes = codes

    def press(self, pad: 'BeePad') -> None:
        if self._codes and len(self._codes) != 0:
            for item in self._codes:
                if isinstance(item, int):
                    pad.consumer_control.release()
                    pad.consumer_control.press(item)
                if isinstance(item, float):
                    sleep(item)

    def release(self, pad: 'BeePad') -> None:
        pad.consumer_control.release()


class LambdaAction(Action):

    def __init__(self, color: int, name: str, callable) -> None:
        super(LambdaAction, self).__init__(name, color)
        self.callable = callable

    def press(self, pad: 'BeePad') -> None:
        self.callable(pad)

    def release(self, pad: 'BeePad') -> None:
        pass


class ResetEncoderAction(Action):

    def __init__(self, color: int, name: str) -> None:
        super(ResetEncoderAction, self).__init__(name, color)

    def press(self, pad: 'BeePad') -> None:
        sleep(5)
        pad.encoder.position = 0

    def release(self, pad: 'BeePad') -> None:
        pass


class Keymap:

    _order = 100

    def __init__(self, name: str=None, order: int=None, actions: 'List[Action]'=[]) -> None:

        Keymap._order += 1
        self.name = name if name else f"? {Keymap._order} ?"
        self.order = order if order else Keymap._order
        self.actions = actions

        # Account for any missing keys or encoder button
        for _ in range(KEYS - len(self.actions)):
            self.actions.append(NullAction())

        # Account for any missing encoder button
        if len(self.actions) < 13:
            self.actions.append(NullAction())

    @staticmethod
    def load_all(dir) -> List(Keymap):

        maps = []

        try:
            files = os.listdir(dir)
        except OSError as err:
            print(err)
            return maps

        for filename in files:
            if filename.endswith('.py') and not filename.startswith('._'):
                try:
                    module = __import__(dir + '/' + filename[:-3])
                    maps.append(Keymap(**module.keymap))
                except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                        IndexError, TypeError) as error:
                    print(f"ERROR {error}, in f{filename}")
                    import traceback
                    traceback.print_exception(error, error, error.__traceback__)

        return maps

