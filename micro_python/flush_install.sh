#!/bin/bash
esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash
esptool.py --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20170105-v1.8.6-296-g5d0d615.bin
