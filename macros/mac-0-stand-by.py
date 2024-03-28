# Placeholder/model

from beepad.keymap import NullAction


keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name" : "Empty",   # Keymap name
    "actions" : [       # List of key actions/macros
        #           COLOR       LABEL     KEY SEQUENCE
        # 1st row  ----------
        NullAction(),
        NullAction(),
        NullAction(),
        # 2nd row ---------
        NullAction(),
        NullAction(),
        NullAction(),
        # 3rd row ----------
        NullAction(),
        NullAction(),
        NullAction(),
        # 4th row ----------
        NullAction(),
        NullAction(),
        NullAction(),
        # Encoder button ---
        NullAction()
    ]
}
