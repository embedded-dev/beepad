VOLUME := /Volumes/CIRCUITPY

RELEASE := 9.x
RELEASE_DATE := 20240326

MODULE_LIB := ${VOLUME}/lib
MODULE_SOURCE := ${HOME}/Projects/CircuitPython/adafruit-circuitpython-bundle-${RELEASE}-mpy-${RELEASE_DATE}/lib
MODULES := \
    adafruit_bus_device \
    adafruit_debouncer.mpy \
    adafruit_display_text \
    adafruit_displayio_sh1106.mpy \
    adafruit_hid \
    adafruit_ticks.mpy \
    neopixel.mpy

APP_LIB := ${VOLUME}/beepad
APP_SOURCE := ./beepad
APP := \
    __init__.py \
    beepad.py \
    beepad_base.py \
    colours.py \
    constants.py \
    display_layout.py \
    keymap.py

TARGETS := $(addprefix ${MODULE_LIB}/, ${MODULES}) \
           $(addprefix ${APP_LIB}/, ${APP}) \
	   ${VOLUME}/code.py \
	   ${VOLUME}/boot.py


install : ${TARGETS}


${MODULE_LIB}/% : ${MODULE_SOURCE}/%
	@echo "$< >>>---> $@"
	/bin/cp -r -X $< $@


${APP_LIB}/% : ${APP_SOURCE}/%
	@echo "$< >>>---> $@"
	/bin/cp -r -X $< $@


${VOLUME}/%.py : ./%.py
	@echo "$< >>>---> $@"
	/bin/cp -r -X $< $@


clear :
	@echo /bin/rm -r -f ${VOLUME}/${LIB}/*


macros : .FORCE
	@echo ""
	@echo ""
	@echo "Volume -"
	@echo "       VOLUME: ${VOLUME}"
	@echo ""
	@echo "Modules -"
	@echo "      RELEASE: ${RELEASE}"
	@echo "         DATE: ${RELEASE_DATE}"
	@echo "       SOURCE: ${MODULE_SOURCE}"
	@echo "          LIB: ${MODULE_LIB}"
	@echo "      MODULES: ${MODULES}"
	@echo ""
	@echo "Application -"
	@echo "      Library: ${APP_LIB}"
	@echo "       Source: ${APP_SOURCE}"
	@echo "        Files: ${APP}"
	@echo ""
	@echo "Targets -"
	@echo "      TARGETS: ${TARGETS}"

.FORCE :
