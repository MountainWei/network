#!/usr/bin/env python
import socket
HOST = '192.168.200.132'
PORT = 50012
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    data = raw_input('Please input data:')
    if data != 'q':
        s.sendall(data)
        data = s.recv(1024)
        print data
    else:
        break
s.close()
