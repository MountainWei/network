#!/usr/bin/env python
import socket
HOST = '192.168.200.132'
PORT = 50012
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    cmd = raw_input('Please input cmd:')
    s.sendall(cmd)
    data = s.recv(1024)
    print data
s.close()
