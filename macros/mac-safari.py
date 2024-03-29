# Macros to implement Finder shortcuts

from beepad.keymap import TypeAction
from adafruit_hid.keycode import Keycode

keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name" : "Safari",  # Keymap name
    "priority" : 90,    # Position priority
    "actions" : [       # List of key actions/macros
        #          COLOR     LABEL        KEY SEQUENCE
        # 1st row  ----------
        TypeAction(0x004000, "< Back",   Keycode.COMMAND, "["),
        TypeAction(0x004000, "Fwd >",    Keycode.COMMAND, "]"),
        TypeAction(0x400000, "Up",       Keycode.SHIFT, " "),
        # 2nd row ----------
        TypeAction(0x202000, "< Tab",    Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB),
        TypeAction(0x202000, "Tab >",    Keycode.CONTROL, Keycode.TAB),
        TypeAction(0x400000, "Down",     " "),
        # 3rd row ----------
        TypeAction(0x000040, "Reload",   Keycode.COMMAND, "r"),
        TypeAction(0x000040, "Home",     Keycode.COMMAND, "H"),
        TypeAction(0x000040, "Private",  Keycode.COMMAND, "N"),
        # 4th row ----------
        TypeAction(0x000000, "Ada",      Keycode.COMMAND, "n", -Keycode.COMMAND,
                                         "www.adafruit.com\n"),
        TypeAction(0x800000, "Digi",     Keycode.COMMAND, "n", -Keycode.COMMAND,
                                         "www.digikey.com\n"),
        TypeAction(0x101010, "Hacks",    Keycode.COMMAND, "n", -Keycode.COMMAND,
                                         "www.hackaday.com\n"),
        # Encoder button ---
        TypeAction(0x000000, "",         Keycode.COMMAND, "w")
    ]
}
