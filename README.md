# 🐝 BeePad 🐝

A MacroPad full of bees.

This is a library for building bee-powered RGB macro keys using the [Adafruit RP2040 Macropad](https://www.adafruit.com/product/5128).

This project is a fork of the [BeePad](https://github.com/trickeydan/beepad) project with extensive changes to support many of the capabilities available from the [Adafruit MacroPad Hotkeys](https://learn.adafruit.com/macropad-hotkeys) project.  But without using the **adafruit_macropad** library and using different classes for the actions instead of overloading Python **lists** and **dictionaries**.

It is written using [CircuitPython](https://circuitpython.org/).

## Usage

You will need to write a `code.py` to define your macros **or** place individual *Keymaps* into a `/macros` directory on the CircuitPython drive.  It is less cumbersome to place them in the `/macros` directory.

Within the limitations of avalable memory and flash storage, an unlimited number of keymaps is supported.

```python
from beepad import BeePad

from beepad.keymap import Keymap, TypeAction

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
    
    ...
    
]}

while True:
    pad.buzz()
```

## Updating

The `boot.py` file disables the serial port and USB flash drive in normal operation.

You can re-enable them by holding the top-left key when resetting the device.

Alternatively you can just not copy the `boot.py` to your device, although this will mean that there is always an additional flash drive connected to your computer, risking corruption of the flash on the RP2040.

## Requirements

The following CircuitPython libraries are required.

You will need to install them in `lib/`.

```
adafruit_bus_device
adafruit_debouncer
adafruit_displayio_sh1106
adafruit_display_text
adafruit_hid.consumer_control
adafruit_hid.consumer_control_code
adafruit_hid.keycode
adafruit_hid.keyboard
adafruit_hid.keyboard_layout_base
adafruit_hid.keyboard_layout_us
adafruit_hid.Mouse
adafruit_simple_text_display
neopixel
```