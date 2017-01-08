import network
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
wlan.active(True)

def scan():
    return wlan.scan()

def is_connected():
    return wlan.isconnected()

def if_config():
    return wlan.ifconfig()
def connect(ssid,password):
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not is_connected():
            pass
    return wlan.ifconfig()

def create_hot():
    ap.active(True)
    ap.config(essid='SUNGU_DA')

def close_hot():
    ap.active(False)

def get_available_networks_html():
    html = """<!DOCTYPE html><html><head> <title>ESP8266 Pins</title> </head><body> <h1>Available Networks</h1><table style="text-align:center;" border="1"> <tr><th>Netowrk</th><th>Connect</th></tr> %s </table></body></html>"""
    scans = scan()
    if scans is not None:
        rows = ["""<tr><td>%s</td><td><a href="/network?name=%s"/>%s</td></tr>""" % ( bssid[0].decode("utf-8"), bssid[0].decode("utf-8"), bssid[0].decode("utf-8")) for bssid in scans]
    else:
        rows = "Now networks Found"

    import gc
    gc.collect()
    response = html % '\n'.join(rows)
    return response
