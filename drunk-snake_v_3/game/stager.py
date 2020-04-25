import time
import socket
import sys
import threading
from queue import Queue
import communication_manager as cm

fail_socket_creation = 0

queue_data = Queue()
queue_id = Queue()

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
        
        ptq = (received_data, address)
        queue_data.put(ptq)
        
    
def sender():
    
    while True:
        
        data_mts_queue = cm.queue_mts.get()
        client_id = int(data_mts_queue[0])
        data = data_mts_queue[1]
        
        connection = connection_list[client_id]
        address = address_list[client_id]
        
        if data == '':
            print("Empty messages are not allowed!")
            
        else:
            send(connection, address, data)
            
            
def get_from_listener():
    
    while True:
        
        gfl = queue_data.get()
        cm.queue_stm.put(gfl)
        

def create_thread_listener(number_of_connections, buffer):
    
    c = 0
    
    while c < number_of_connections:
        
        connection = connection_list[c]
        address = address_list[c]
        
        t = threading.Thread(target=listener, args=(connection, address, buffer))
        t.daemon = True
        t.start()
        
        c += 1
        
        
def create_thread_sender():
        
    t = threading.Thread(target=sender)
    t.daemon = True
    t.start()
    

def create_thread_get_from_listener():
        
    t = threading.Thread(target=get_from_listener)
    t.daemon = True
    t.start()
        

def start_stager(prt, number_of_connections, notimeout=False):
    
    create_socket(prt)
    setting_up_connections(number_of_connections, notimeout)
    
    
def start_listener(number_of_connections, buffer):
    
    try:
        create_thread_listener(number_of_connections, buffer)
    
    except Exception:
        print("Error when creating listener thread, are the connections set?")
        
        
def start_sender():
    
    try:
        create_thread_sender()
    
    except Exception:
        print("Error when creating sender thread, are the connections set?")
        
def start_get_from_listener():
    
    try:
        create_thread_get_from_listener()
    
    except Exception:
        print("Error when creating get-from-listener thread, are the connections set?")


#Usage:
#stager.start_stager(4444, 2) # <-- port and number of clients
#stager.start_listener(2, 256) # <-- number of clients and buffer size for sent data
#stager.start_sender() # <-- start the sender ######main###### --> cm.queue_mts.put((ID, 'data'))
#stager.start_get_from_listener() # <-- start the method that delivers sent data to main ######main###### --> cm.queue_stm.get()

