# Macros for media commands

from beepad.keymap import ConsumerControlAction, NullAction
from adafruit_hid.consumer_control_code import ConsumerControlCode

keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name" : "Media",   # Keymap name
    "priority" : 50,    # Position priority
    "actions" : [       # List of key actions/macros
        #                     COLOR     LABEL    KEY SEQUENCE
        # 1st row ----------
        NullAction(),
        ConsumerControlAction(0x000020, "Vol+",  ConsumerControlCode.VOLUME_INCREMENT),
        ConsumerControlAction(0x202020, "Brt+",  ConsumerControlCode.BRIGHTNESS_INCREMENT),
        # 2nd row ----------
        NullAction(),
        ConsumerControlAction(0x000020, "Vol-",  ConsumerControlCode.VOLUME_DECREMENT),
        ConsumerControlAction(0x202020, "Brt-",  ConsumerControlCode.BRIGHTNESS_DECREMENT),
        # 3rd row ----------
        NullAction(),
        ConsumerControlAction(0x200000, "Mute",  ConsumerControlCode.MUTE),
        NullAction(),
        # 4th row ----------
        ConsumerControlAction(0x202000, "<<",    ConsumerControlCode.SCAN_PREVIOUS_TRACK),
        ConsumerControlAction(0x002000, "Play",  ConsumerControlCode.PLAY_PAUSE),
        ConsumerControlAction(0x202000, ">>",    ConsumerControlCode.SCAN_NEXT_TRACK),
        # Encoder button ---
        NullAction()
    ]
}
