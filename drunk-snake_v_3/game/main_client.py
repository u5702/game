import time
import game_classes as game
import board
import client
import threading
from queue import Queue
import communication_manager as cm

x__x__x_self_ID_x__x__x = 'client#sys'


def get_name():
    
    name = input("Gib deinen Namen ein (max. 10 Zeichen!):  ")
    
    if len(name) > 10:
        print("Der eingegebene Name war zu lange!")
        get_name()
    
    else:
        return str(name)


client.start_listener(256) # <-- buffer size for sent data
client.start_sender() # <-- start the sender ######main###### --> cm.queue_mtc.put('data')
client.start_get_from_listener() # <-- start the method that delivers sent data to main ######main###### --> cm.queue_ctm.get()

while True:
    
    adata = cm.queue_ctm.get()
    
    if adata == 'name_request':
        name = get_name()
        cm.queue_mtc.put(name)
    
    elif adata == 'sys_info':
        bdata = cm.queue_ctm.get()
        print(bdata)
        
    elif adata == 'sys_field':
        bdata = cm.queue_ctm.get()
        fieldnumber = "board_client/field" + bdata + ".txt"
        
        a_f = open(fieldnumber, "r")

        for line in a_f:

            print(line)
        
        a_f.close()
        
    elif adata == 'sys_action':
        bdata = cm.queue_ctm.get()
        print(bdata)
        print("Du kannst " + bdata + " Schlücke verteilen\n")
        print("Möchtest du an jemanden Schlücke verteilen?")
        ts = time.time()
        aw = input("(y/n): ")
        
        if time.time() - ts > 12:
            print("Du warst zu langsam!")
            
        else:
            
            if aw == 'N' or aw == 'n' or aw == '':
                cm.queue_mtc.put('sys_no')
                
            elif aw == 'Y' or aw == 'y':
                cm.queue_mtc.put('sys_yes')
                time.sleep(0.3)
                ldata = cm.queue_ctm.get()
                print(ldata)
                ts = time.time()
                
                aw_2 = "_1_:: " + input("An wen? (Zahl angeben): ")
                aw_2_2 = "_2_:: " + input("Wie viele? (max. {}): " .format(bdata))
                
                if time.time() - ts > 12:
                    print("Du warst zu langsam!")
                    
                else:
                    
                    cm.queue_mtc.put(aw_2)
                    time.sleep(0.5)
                    cm.queue_mtc.put(aw_2_2)
            
            else:
                cm.queue_mtc.put('sys_no')
                print("Hosch gsoffa?!")
            
    
    elif adata == 'sys_won':
        print("Gewonnen!")
        break
                
        
    else:
        
        continue
    
while True:
    
    adata = cm.queue_ctm.get()
    
    if adata == 'sys_info':
        bdata = cm.queue_ctm.get()
        print(bdata)
        
    elif adata == 'sys_field':
        bdata = cm.queue_ctm.get()
        fieldnumber = "board_client/field" + bdata + ".txt"

print("Finished")