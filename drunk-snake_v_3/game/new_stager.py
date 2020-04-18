import time
import socket
import os


host = ''
port = 5556
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

        
s.listen(1)
(connection, address) = s.accept()
 
if os.fork() == 0:
    
    while True:
        
        data = connection.recv(256)
        print(data, address[0])
        
        if data == b'':
        
            os._exit(0)
else:
    
    while True:

        cmd = input("Command: ")
        rawdata = bytes(cmd, 'utf-8')
        connection.send(rawdata)
