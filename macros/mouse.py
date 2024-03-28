# Macros to emulate a three button mouse

from beepad.keymap import MouseAction, NullAction
from adafruit_hid.Mouse import Mouse


keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name" : "Mouse",   # Keymap name
    "actions" : [       # List of key actions/macros
        #           COLOR     LABEL     KEY SEQUENCE
        # 1st row ----------
        MouseAction(0x200000, "L",      buttons=Mouse.LEFT_BUTTON),
        MouseAction(0x202000, "M",      buttons=Mouse.MIDDLE_BUTTON),
        MouseAction(0x002000, "R",      buttons=Mouse.RIGHT_BUTTON),
        # 2nd row ----------
        NullAction(),
        MouseAction(0x202020, "Up",     y=-10),
        NullAction(),
        # 3rd row ----------
        MouseAction(0x202020, "Left",   x=-10),
        NullAction(),
        MouseAction(0x202020, "Right",  x=10),
        # 4th row ----------
        NullAction(),
        MouseAction(0x202020, "Down",   y=10),
        NullAction(),
        # Encoder button ---
        NullAction()
    ]
}
