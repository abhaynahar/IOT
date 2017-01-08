import ure
import picoweb
import wlan

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    if not wlan.is_connected():
      yield from resp.awrite("HTTP/1.0 200 OK\r\n")
      yield from resp.awrite("Content-Type: text/html\r\n")
      yield from resp.awrite("\r\n")
      rows = wlan.get_available_networks_html();
      print(rows)
      yield from resp.awrite(str(rows))
    else:
      print("********",req)
      wlan.close_hot()
      yield from resp.awrite("HTTP/1.0 200 OK\r\n")
      yield from resp.awrite("Content-Type: text/html\r\n")
      yield from resp.awrite("\r\n")
      yield from resp.awrite("connected %s" % (str(wlan.if_config())) )


@app.route("/network")
def network(req, resp):
    req.parse_qs()
    print("******** ",req.form)
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    yield from resp.awrite("""<!DOCTYPE html><html><head><title>ESP8266 Pins</title></head><body><h1>Connect</h1><br><form class="" action="/connect" ><label>%s</label><input type="hidden" name="ssid" value="%s"/><input type="password" name="password" value=""/><input type="submit" value="Connect"/></form></body></html>""" % (req.form["name"][0], req.form["name"][0]) )

@app.route("/connect")
def connect(req, resp):
    req.parse_qs()
    print("******** ",req.form)
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    config = wlan.connect(req.form['ssid'][0], req.form['password'][0])
    yield from resp.awrite("""<!DOCTYPE html><html><head><title>ESP8266 Pins</title></head><body><h1>Change your network and click</h1><a href="http://%s">Go</a></body></html>""" % (str(config[0])) )

wlan.scan()
print(wlan.is_connected())
if not wlan.is_connected():
    wlan.create_hot()

app.run(debug=True)
