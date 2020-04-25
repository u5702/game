import time
import socket
import sys
import threading
from queue import Queue
import communication_manager


queue_i = Queue()

f = open("config/connection_config.txt", "r")

for line in f:
    
    exec('{}' .format(line))

f.close()

host = server_ip
port = server_port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b'Hello Server! It is Client.')


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


def listener(buffer, s=s):
    
    while True:
        
        received_data = receive(buffer)
        
        if received_data == '' or b'':
            break
        
        ptq = received_data
        
        queue_i.put(ptq)
        
        
def sender():
    
    while True:
    
        data = input("Input: ")
        
        if data == '':
            print("Empty messages are not allowed!")
            
        else:
            send(data)
        time.sleep(1)

def create_thread_listener(buffer, s=s):
   
    t = threading.Thread(target=listener, args=(buffer, s))
    t.daemon = True
    t.start()


def create_thread_sender():
   
    t = threading.Thread(target=sender)
    t.daemon = True
    t.start()
    

def get_from_listener():
    
    while True:
        
        gfl = queue_i.get()
        
        if gfl == 'error-break-now':
            
            s.close()
            print("Connection closed, due to no signal!")
            
        else:
            print(gfl)

        
def start_listener(buffer):
    
    try:
        create_thread_listener(buffer)
    
    except Exception:
        print("Error when creating listener thread, are the connections set?")
        
start_listener(256)
create_thread_sender()
get_from_listener()
