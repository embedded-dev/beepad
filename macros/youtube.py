# Macros to control a YouTube Safari on macOS
#
# There doesn't appear to be any keyboad commands which can skip the ads.

from beepad.keymap import TypeAction, NullAction
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


keymap = {   # REQUIRED dictionary - must be named "keymap"
    'name': "YouTube",  # Keymap name
    'actions': [        # list of key actions/macros
        #          COLOR     LABEL       KEY SEQUENCE
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
    ]
}
