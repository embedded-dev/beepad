import os
import board
import digitalio
import displayio
import storage
import usb_cdc

from time import sleep


key1 = digitalio.DigitalInOut(board.KEY1)
key1.switch_to_input(pull=digitalio.Pull.UP)


try:
    os.stat('/develop')
except:
    develop = False
else:
    develop = True


if develop or not key1.value:
    print("Development mode")
    sleep(5)
else:
    print("Functional mode")
    displayio.release_displays()
    usb_cdc.disable()
    storage.disable_usb_drive()

try:
    import usb_midi
except ImportError:
    pass
else:
    usb_midi.disable()
