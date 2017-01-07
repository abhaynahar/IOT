ampy --port /dev/cu.SLAB_USBtoUART mkdir lib/logging#!/bin/bash
ampy --port /dev/cu.SLAB_USBtoUART mkdir lib
echo "lib created"
ampy --port /dev/cu.SLAB_USBtoUART mkdir lib/picoweb
echo "lib/picoweb created"
ampy --port /dev/cu.SLAB_USBtoUART put lib/picoweb/__init__.py lib/picoweb/__init__.py
echo "lib/picoweb init copied"
ampy --port /dev/cu.SLAB_USBtoUART put lib/picoweb/utils.py lib/picoweb/utils.py
echo "lib/picoweb utils copied"

ampy --port /dev/cu.SLAB_USBtoUART mkdir lib/uasyncio
echo "lib/usaync created"
ampy --port /dev/cu.SLAB_USBtoUART put lib/uasyncio/__init__.py lib/uasyncio/__init__.py
echo "lib/uasync init copied"
ampy --port /dev/cu.SLAB_USBtoUART put lib/uasyncio/core.py lib/uasyncio/core.py
echo "lib/uasync core copied"


ampy --port /dev/cu.SLAB_USBtoUART put lib/logging.py lib/logging.py
echo "lib/logging logging copied"
ampy --port /dev/cu.SLAB_USBtoUART reset
