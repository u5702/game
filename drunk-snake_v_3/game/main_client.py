import time
import game_classes as game
import board
import client
import threading
from queue import Queue
import communication_manager as cm


client.start_listener(256) # <-- buffer size for sent data
client.start_sender() # <-- start the sender ######main###### --> cm.queue_mtc.put('data')
client.start_get_from_listener() # <-- start the method that delivers sent data to main ######main###### --> cm.queue_ctm.get()

while True:
    
    adata = cm.queue_ctm.get()
    
    if adata == 'name_request':
        name = input("Gib deinen Namen ein:  ")
        cm.queue_mtc.put(name)
        
    elif adata == 'sys_won':
        print("Gewonnen!")
        break
    
    elif adata == 'sys_r_nmbr':
        print("falsche Nummer")
        
    else:
        
        print(adata)
        #fieldnumber = "board/field" + adata + ".txt"
        #a_f = open(fieldnumber, "r")

        #for line in a_f:
            
            #exec('{}' .format(line))
        
        #a_f.close()
        
    
    
print("Finished")