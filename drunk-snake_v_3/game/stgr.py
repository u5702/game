import time
import socket
import os

#class sockt:
    
#    def __init__(self, prt=5555):
#        
#        self.host = ''
#        self.port = prt
#        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        self.connection = ""
#        self.address = ""
        
#        self.s.bind((host, port))
    
#    def sockt_listen(self):
        
#        self.s.listen(1)
#        (self.connection, self.address) = self.s.accept()
        
    
#def create_socket(prt=5555):
#    host = ''
#    port = prt
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.bind((host, port))

#def listen_socket():
#    s.listen(1)
#    (connection, self.address) = s.accept()


host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

x_con = 0



    
while x_con < x:
        
    s.listen(1)
    (connection, address) = s.accept()
        
    if 0 == os.fork():
            
        while True:
                
            data = connection.recv(256)
            print(data, address[0])
            cmd = rd.read()
            rawdata = bytes(cmd, 'utf-8')
            connection.send(rawdata)
            data = connection.recv(256)
            print(data, address[0])
                
                
            if data == b'':
                    
                os._exit(0)