"""Save this file as code.py."""
from beepad import BeePad
from beepad.keymap import Keymap, MouseAction, TypeAction, LambdaAction, NullAction, ConsumerControlAction
from adafruit_hid.Mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode


def hello(ignore: BeePad):
    print("Hello, world!")

def hello_name(pad: BeePad):
    keymap = pad.current_keymap
    print("Hello, {}".format(keymap.name))


pad = BeePad([

    {'name': "Git",
     'actions': [
        #          COLOR     LABEL     KEY SEQUENCE
        # 1st row ----------
        TypeAction(0xff0000, "gst",    "git status\n"),
        TypeAction(0x00ff00, "gc",     "git commit\n"),
        TypeAction(0x0000ff, "gc -m",  "git commit -m @"),
        # 2nd row ----------
        TypeAction(0x0000ff, "gca!",   "git commit --amend\n"),
        TypeAction(0x00ff00, "gd",     "git diff \n"),
        TypeAction(0xff0000, "gd -s",  "git diff --staged\n"),
        # 3rd row ----------
        TypeAction(None,     "ga .",   "git add .\n"),        
        TypeAction(None,     "ggpush", "git push origin $(git rev-parse --abbrev-ref HEAD)\n"),
        TypeAction(None,     "ggpull", "git pull origin $(git rev-parse --abbrev-ref HEAD)\n"),
        # 4th row ----------
        TypeAction(0xff0000, "main",   "git checkout main\n"),
        TypeAction(0x00ff00, "grm",    "git rebase origin/main\n"),
        TypeAction(0x0000ff, "dgt",    "git checkout -b dgt/"),
        # Encoder button ---
        NullAction()
    ]},

    {'name': "Mouse",
     'actions': [
        #           COLOR     LABEL     KEY SEQUENCE
        # 1st row ----------
        MouseAction(0x200000, 'L',      buttons=Mouse.LEFT_BUTTON),
        MouseAction(0x202000, 'M',      buttons=Mouse.MIDDLE_BUTTON),
        MouseAction(0x002000, 'R',      buttons=Mouse.RIGHT_BUTTON),
        # 2nd row ----------
        NullAction(),
        MouseAction(0x202020, 'Up',     y=-10),
        NullAction(),
        # 3rd row ----------
        MouseAction(0x202020, 'Left',   x=-10),
        NullAction(),
        MouseAction(0x202020, 'Right',  x=10),
        # 4th row ----------
        NullAction(),
        MouseAction(0x202020, 'Down',   y=10),
        NullAction(),
        # Encoder button ---
        NullAction()
    ]},

    {'name': "Keypad",
     'actions': [
        #          COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        TypeAction(0x202000, '7',        '7'),
        TypeAction(0x202000, '8',        '8'),
        TypeAction(0x202000, '9',        '9'),
        # 2nd row ----------
        TypeAction(0x202000, '4',        '4'),
        TypeAction(0x202000, '5',        '5'),
        TypeAction(0x202000, '6',        '6'),
        # 3rd row ----------
        TypeAction(0x202000, '1',        '1'),
        TypeAction(0x202000, '2',        '2'),
        TypeAction(0x202000, '3',        '3'),
        # 4th row ----------
        TypeAction(0x101010, '*',        '*'),
        TypeAction(0x800000, '0',        '0'),
        TypeAction(0x101010, '#',        '#'),
        # Encoder button ---
        TypeAction(0x000000, '',         Keycode.BACKSPACE)
    ]},

    {'name': "Media",
     'actions': [
        #                     COLOR     LABEL         KEY SEQUENCE
        # 1st row ----------
        NullAction(),
        ConsumerControlAction(0x000020, 'Vol+',       ConsumerControlCode.VOLUME_INCREMENT),
        ConsumerControlAction(0x202020, 'Bright+',    ConsumerControlCode.BRIGHTNESS_INCREMENT),
        # 2nd row ----------
        NullAction(),
        ConsumerControlAction(0x000020, 'Vol-',       ConsumerControlCode.VOLUME_DECREMENT),
        ConsumerControlAction(0x202020, 'Bright-',    ConsumerControlCode.BRIGHTNESS_DECREMENT),
        # 3rd row ----------
        NullAction(),
        ConsumerControlAction(0x200000, 'Mute',       ConsumerControlCode.MUTE),
        NullAction(),
        # 4th row ----------
        ConsumerControlAction(0x202000, '<<',         ConsumerControlCode.SCAN_PREVIOUS_TRACK),
        ConsumerControlAction(0x002000, 'Play/Pause', ConsumerControlCode.PLAY_PAUSE),
        ConsumerControlAction(0x202000, '>>',         ConsumerControlCode.SCAN_NEXT_TRACK),
        # Encoder button ---
        NullAction()
    ]},

    {'name': 'YouTube', 
     'actions': [
        # COLOR    LABEL       KEY SEQUENCE
        # 1st row  ----------
        TypeAction(0x020000, 'Mute',     'm'),                 # Toggles Mute
        TypeAction(0x020200, 'Full',     'f'),                 # Toggle Full Screen Mode
        TypeAction(0x020200, 'Caption',  'c'),                 # Toggles Captions
        # 2nd row  ---------
        TypeAction(0x000202, '<Prev',    Keycode.SHIFT, 'p'),  # If in Playlist goes to previous video in playlist, else inop
        TypeAction(0x020200, 'Theater',  't'),                 # Toggle Theater Mode
        TypeAction(0x000202, 'Next>',    Keycode.SHIFT, 'n'),  # If in Playlist goes to next video in playlist, else next suggested video
        # 3rd row  ----------
        TypeAction(0x000202, '<5s',      Keycode.LEFT_ARROW),  # Skips back five seconds
        TypeAction(0x000400, 'Play',     'k'),                 # Toggles Play
        TypeAction(0x000202, '5s>',      Keycode.RIGHT_ARROW), # Skips forward five seconds
        # 4th row  ----------
        TypeAction(0x000202, '<1F',      ','),                 # If paused skips backward 1 frame
        TypeAction(0x020200, 'Mini',     'i'),                 # Toggles MiniPlayer
        TypeAction(0x000202, '1F>',      '.'),                 # If paused skips forward 1 frame
        # Encoder button ----
        NullAction()
    ]},

    {'name': 'Finder',
     'actions': [   # List of button macros...
        # COLOR    LABEL       KEY SEQUENCE
        # 1st row ----------
        TypeAction(0x000004, 'Safari',   Keycode.COMMAND, ' ', 0.5, 'Safari.app', 0.1, Keycode.RETURN),
        TypeAction(0x020000, 'New',      Keycode.COMMAND, 'n'),
        TypeAction(0x000202, 'Siri',     Keycode.CONTROL, Keycode.COMMAND, ' '),
        # 2nd row ---------
        TypeAction(0x000004, 'Notes',    Keycode.COMMAND, ' ', 0.5, 'Notes.app', 0.1, Keycode.RETURN),
        TypeAction(0x020000, 'NewTab',   Keycode.COMMAND, "t"),
        TypeAction(0x000202, 'Dict',     Keycode.CONTROL, "d"),
        # 3rd row ----------
        TypeAction(0x000004, 'Mu Edit',  Keycode.COMMAND, ' ', 0.5, 'Mu Editor', 0.1, Keycode.RETURN),
        TypeAction(0x000004, 'KSP',      Keycode.COMMAND, ' ', 0.5, 'KSP', 0.1, Keycode.RETURN),
        TypeAction(0x020200, 'FGrab',    Keycode.COMMAND, Keycode.SHIFT, "3"),
        # 4th row ----------
        TypeAction(0x000004, 'Mssgs',    Keycode.COMMAND, ' ', 0.5, 'Messages.app', 0.1, Keycode.RETURN),
        TypeAction(0x000004, 'Calc',     Keycode.COMMAND, ' ', 0.5, 'Calculator.app', 0.1, Keycode.RETURN),
        TypeAction(0x020200, 'SShot',    Keycode.COMMAND, ' ', 0.5, 'Screenshot.app', 0.1, Keycode.RETURN),
        # Encoder button ---
        NullAction()
    ]}

    # Add more keymaps here!

])

while True:
    pad.buzz()