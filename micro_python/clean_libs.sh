
ampy --port /dev/cu.SLAB_USBtoUART rm lib/picoweb/__init__.py
echo "lib/picoweb init deleted"
ampy --port /dev/cu.SLAB_USBtoUART rm lib/picoweb/utils.py
echo "lib/picoweb utils deleted"

ampy --port /dev/cu.SLAB_USBtoUART rm lib/uasyncio/__init__.py
echo "lib/uasync init deleted"
ampy --port /dev/cu.SLAB_USBtoUART rm lib/uasyncio/core.py
echo "lib/uasync core deleted"


ampy --port /dev/cu.SLAB_USBtoUART rm lib/logging.py
echo "lib/logging logging deleted"



ampy --port /dev/cu.SLAB_USBtoUART rm lib/wlan/__init__.py
echo "lib/wlan __init__ deleted"


ampy --port /dev/cu.SLAB_USBtoUART rm boot.py
