import time
import socket
import sys
import threading
from queue import Queue
import communication_manager

queue_intern = Queue()

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
        
        to_put = received_data
        
        queue_intern.put(to_put)


def create_thread_listener(buffer, s=s):
   
    t = threading.Thread(target=listener, args=(buffer, s))
    t.daemon = True
    t.start()


def get_from_listener():
    
    while True:
        
        got_from_listener = queue_intern.get()
        
        if got_from_listener == 'error-break-now':
            
            s.close()
            print("Connection closed, due to no signal!")
            
        else:
            print(got_from_listener)


def start_sender():
    
    while True:
    
        data = input("Input: ")
        
        if data == '':
            print("Empty messages are not allowed!")
            
        else:
            send(data)
        
def start_listener(buffer):
    
    try:
        create_thread_listener(buffer)
    
    except Exception:
        print("Error when creating listener thread, are the connections set?")
        
start_listener(256)
get_from_listener()
start_sender()