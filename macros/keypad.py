# Macros to implement a phone keypad

from beepad.keymap import TypeAction
from adafruit_hid.keycode import Keycode


keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name" : "Keypad",  # Keymap name
    "priority" : 30,    # Position priority
    "actions" : [       # List of key actions/macros
        #          COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        TypeAction(0x202000, "7",        "7"),
        TypeAction(0x202000, "8",        "8"),
        TypeAction(0x202000, "9",        "9"),
        # 2nd row ----------
        TypeAction(0x202000, "4",        "4"),
        TypeAction(0x202000, "5",        "5"),
        TypeAction(0x202000, "6",        "6"),
        # 3rd row ----------
        TypeAction(0x202000, "1",        "1"),
        TypeAction(0x202000, "2",        "2"),
        TypeAction(0x202000, "3",        "3"),
        # 4th row ----------
        TypeAction(0x101010, "*",        "*"),
        TypeAction(0x800000, "0",        "0"),
        TypeAction(0x101010, "#",        "#"),
        # Encoder button ---
        TypeAction(0x000000, "",         Keycode.BACKSPACE)
    ]
}
