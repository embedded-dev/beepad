# Macros to test the "LambdaAction" functionality

from beepad import BeePad
from beepad.keymap import LambdaAction


def hello_world(ignore: BeePad):
    print("Hello, world!")

def hello_name(pad: BeePad):
    keymap = pad.current_keymap
    print("Hello, {}".format(keymap.name))


keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name" : "Lambda",  # Keymap name
    "actions" : [       # List of key actions/macros
        #           COLOR       LABEL     KEY SEQUENCE
        # 1st row  ----------
        LambdaAction(0x00ff00, "Hello",   hello_world),
        LambdaAction(0xff0000, "Hello",   hello_name),
    ]
}
