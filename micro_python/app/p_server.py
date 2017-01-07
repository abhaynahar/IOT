import ure
import picoweb
import logging



logging.basicConfig(level=logging.DEBUG)
app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    print("********",req)
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    yield from resp.awrite("<form action=\"/squares\"><input type=\"text\" name=\"firstname\" value=\"Mickey\"><input type=\"submit\" value=\"Submit\"></form>")


@app.route("/squares")
def index(req, resp):
    req.parse_qs()
    print("******** - squares",req.form)
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    yield from resp.awrite("OK")


app.run(debug=True)
