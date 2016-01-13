#!/usr/bin/env python
import socket
import sys

HOST = '192.168.200.132'
PORT = 50012
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket,Error code: ' + str(msg[0]) + ', Error message: ' + msg[1]
    sys.exit()

print 'Socket Created.'

s.bind((HOST, PORT))
print 'Socket bind complete'
s.listen(5)
print 'Socket is listening now.'

try:
    while True:
        conn, addr = s.accept()
        print 'Connected by', addr
        while True:
            data = conn.recv(1024)
            if not data:
                conn.close()
                break
            print ('[Client %s:%s said]:%s' % (addr[0], addr[1], data))
            reply = 'server has received your message.'
            conn.sendall(reply)
        conn.close()

finally:
    s.close()

