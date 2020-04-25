import time
import socket
import sys
import threading
from queue import Queue
import communication_manager

fail_socket_creation = 0

queue_intern = Queue()

connection_list = []
address_list = []

def create_socket(prt):
    
    global host
    global port
    global s
    global fail_socket_creation
    
    try:
        host = ''
        port = prt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))

    except socket.error as msg:
        print("Error when creating the socket: " + str(msg), "\n")
        fail_socket_creation += 1
        
        if fail_socket_creation < 5:
            print("trying again to create the socket...")
            create_socket()


def setting_up_connections(number_of_connections, notimeout=False):
    
    for i in connection_list:
        i.close()

    del connection_list[:]
    del address_list[:]
    
    already_set = 1
    while already_set <= number_of_connections:
        
        try:
            s.listen(1)
            (connection, address) = s.accept()
            
            if notimeout == True:
                s.setblocking(1) #Blocking connection-timeout

            connection_list.append(connection)
            address_list.append(address)

            print("A connection has been established to: " + address[0])

        except:
            print("Error when accepting connections")
            break
            
        already_set += 1


def close_connections():
    
    for i in connection_list:
        i.close()
    
    print("All connections are closed!")


def receive(connection, address, buffer, mode='message'):
    
    rawdata = connection.recv(buffer)
    
    if mode == 'message':
        data = rawdata.decode('utf-8')
    
    elif mode == 'raw':
        data == rawdata
        
    else:
        print("Error: no such mode available")
   
    return data
    

def send(connection, address, data):

    rawdata = bytes(data, 'utf-8')
    connection.send(rawdata)
    
    
def listener(connection, address, buffer):
    
    while True:
        
        received_data = receive(connection, address, buffer)
        
        if received_data == '' or b'':
            print("Error, connection closed ", address)
            break
        
        to_put = (received_data, address)
        
        queue_intern.put(to_put)
        

def create_thread_listener(number_of_connections, buffer):
    
    c = 0
    
    while c < number_of_connections:
        
        connection = connection_list[c]
        address = address_list[c]
        
        t = threading.Thread(target=listener, args=(connection, address, buffer))
        t.daemon = True
        t.start()
        
        c += 1
        

def start(prt, number_of_connections, notimeout=False):
    
    create_socket(prt)
    setting_up_connections(number_of_connections, notimeout)
    
    
def start_listener(number_of_connections, buffer):
    
    try:
        create_thread_listener(number_of_connections, buffer)
    
    except Exception:
        print("Error when creating listener thread, are the connections set?")
    

def get_from_listener():
    
    while True:
        
        got_from_listener = queue_intern.get()
        print(got_from_listener)
        
        
def los():
    start(4444, 2)
    start_listener(2, 256)
    data = communication_manager.queue_mts.get()
    send(connection_list[0], address_list[0], data)
    get_from_listener()