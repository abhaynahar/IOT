import network
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
wlan.active(True)

def scan():
    return wlan.scan()

def is_connected():
    return wlan.isconnected()

def connect(ssid,password):
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not is_connected():
            pass
    return wlan.ifconfig()

def create_hot():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='SUNGU_DA')
