import ure
import picoweb
import logging



logging.basicConfig(level=logging.DEBUG)
app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    import wlan
    scans = wlan.scan()
    if not wlan.is_connected():
      yield from resp.awrite("HTTP/1.0 200 OK\r\n")
      yield from resp.awrite("Content-Type: text/html\r\n")
      yield from resp.awrite("\r\n")
      rows = ['<tr><td>%s</td></tr>' % ( bssid[0].decode("utf-8")) for bssid in wlan.scan()]
      print(rows)
      yield from resp.awrite(str(rows))
    else:
      print("********",req)
      yield from resp.awrite("HTTP/1.0 200 OK\r\n")
      yield from resp.awrite("Content-Type: text/html\r\n")
      yield from resp.awrite("\r\n")
      yield from resp.awrite("connected")


@app.route("/squares")
def index(req, resp):
    req.parse_qs()
    print("******** - squares",req.form)
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    yield from resp.awrite("OK")


import wlan
wlan.scan()
print(wlan.is_connected())
if not wlan.is_connected():
    wlan.create_hot()

app.run(debug=True)
