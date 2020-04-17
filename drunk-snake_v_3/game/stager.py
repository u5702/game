import time
import socket
import multiprocessing
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

con_set = 0

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def child(id, connection_tuple):
    
    print("child ", id)
    
    f = open("log/stager_child_processes.txt", "a")
    PID = os.getpid()
    exec('f.write("{}:{}")' .format(PID, id))
    f.write("\n")
    f.flush
    f.close
    
    connection = connection_tuple[0]
    address = connection_tuple[1]
    while True:
        
        data = connection.recv(256)
        if data == b'':
            break
        print(data, address[0], id)
        #exec('cmd = ptc{}.get()' .format(id))
        #rawdata = bytes(cmd, 'utf-8')
        #connection.send(rawdata)
        #data = connection.recv(256)
        #print(data, address[0])


def stgr(mts, stm, x):
    
    
    x_con = 1
    while x_con <= x:
        
        s.listen(1)
        (connection, address) = s.accept()
        
        exec('ptc{} = multiprocessing.Queue()' .format(x_con))
        child_proc = multiprocessing.Process(target=child, args=(x_con, (connection, address)))
        child_proc.start()
        time.sleep(0.5)
        
        if x_con == x:
            global con_set
            con_set = 1
            
        
        x_con += 1