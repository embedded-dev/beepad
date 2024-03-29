# Macros to implement macOS Finder shortcuts

from beepad.keymap import TypeAction, NullAction
from adafruit_hid.keycode import Keycode

keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name" : "Finder",  # Keymap name
    "priority" : 100,   # Position priority
    "actions" : [       # List of key actions/macros
        #          COLOR     LABEL        KEY SEQUENCE
        # 1st row  ----------
        TypeAction(0x000004, "Safari",   Keycode.COMMAND, " ", 0.5, "Safari.app", 0.1, Keycode.RETURN),
        TypeAction(0x020000, "New",      Keycode.COMMAND, "n"),
        TypeAction(0x000202, "Siri",     Keycode.CONTROL, Keycode.COMMAND, " "),
        # 2nd row ---------
        TypeAction(0x000004, "Notes",    Keycode.COMMAND, " ", 0.5, "Notes.app", 0.1, Keycode.RETURN),
        TypeAction(0x020000, "NewTab",   Keycode.COMMAND, "t"),
        TypeAction(0x000202, "Dict",     Keycode.CONTROL, "d"),
        # 3rd row ----------
        TypeAction(0x000004, "MuEdit",   Keycode.COMMAND, " ", 0.5, "Mu Editor", 0.1, Keycode.RETURN),
        TypeAction(0x000004, "KSP",      Keycode.COMMAND, " ", 0.5, "KSP", 0.1, Keycode.RETURN),
        TypeAction(0x020200, "FGrab",    Keycode.COMMAND, Keycode.SHIFT, "3"),
        # 4th row ----------
        TypeAction(0x000004, "Mssgs",    Keycode.COMMAND, " ", 0.5, "Messages.app", 0.1, Keycode.RETURN),
        TypeAction(0x000004, "Calc",     Keycode.COMMAND, " ", 0.5, "Calculator.app", 0.1, Keycode.RETURN),
        TypeAction(0x020200, "SShot",    Keycode.COMMAND, " ", 0.5, "Screenshot.app", 0.1, Keycode.RETURN),
        # Encoder button ---
        NullAction()
    ]
}
