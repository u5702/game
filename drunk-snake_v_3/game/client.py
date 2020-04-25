import time
import socket
import sys
import threading
from queue import Queue
import communication_manager as cm


queue_data = Queue()


f = open("config/connection_config.txt", "r")

for line in f:
    
    exec('{}' .format(line))

f.close()

host = server_ip
port = server_port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#s.send(b'Hello Server! It is Client.')



def close_connection():
    
    s.close()
    print("Connection is closed!")


def receive(buffer, mode='message', s=s):
    
    rawdata = s.recv(buffer)
    
    if mode == 'message':
        data = rawdata.decode('utf-8')
    
    elif mode == 'raw':
        data == rawdata
        
    else:
        print("Error: no such mode available")
   
    return data


def send(data, s=s):

    rawdata = bytes(data, 'utf-8')
    s.send(rawdata)


def listener(a, buffer, s=s):
    
    while True:
        
        received_data = receive(buffer)
        
        if received_data == '' or b'':
            print("Error, connection closed ")
            break
        
        ptq = received_data
        queue_data.put(ptq)


def sender():
    
    while True:
    
        data = cm.queue_mtc.get()
        
        if data == '':
            print("Empty messages are not allowed!")
            
        else:
            send(data)


def get_from_listener():
    
    while True:
        
        gfl = queue_data.get()
        cm.queue_ctm.put(gfl)
        
        
def create_thread_listener(buffer):
               
    t = threading.Thread(target=listener, args=('a', buffer))
    t.daemon = True
    t.start()
        
        
def create_thread_sender():
    
    t = threading.Thread(target=sender)
    t.daemon = True
    t.start()
    

def create_thread_get_from_listener():
        
    t = threading.Thread(target=get_from_listener)
    t.daemon = True
    t.start()
    
  
def start_listener(buffer):
    
    try:
        create_thread_listener(buffer)
    
    except Exception:
        print("Error when creating listener thread, is the connection set?")
        
        
def start_sender():
    
    try:
        create_thread_sender()
    
    except Exception:
        print("Error when creating sender thread, is the connection set?")


def start_get_from_listener():
    
    try:
        create_thread_get_from_listener()
    
    except Exception:
        print("Error when creating get-from-listener thread, is the connection set?")


#Usage:
#client.start_listener(256) # <-- buffer size for sent data
#client.start_sender() # <-- start the sender ######main###### --> cm.queue_mtc.put('data')
#client.start_get_from_listener() # <-- start the method that delivers sent data to main ######main###### --> cm.queue_ctm.get()