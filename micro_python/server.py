import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('ssid', 'pass')

import machine
import ure
import uio as IO
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]


import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    my_file = IO.open('index.html', 'r')
    html = ""
    for line in my_file:
        html += str(line)
    print(html)
    response = html
    cl.send(response)
    cl.close()
