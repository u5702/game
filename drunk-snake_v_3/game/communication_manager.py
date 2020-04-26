from queue import Queue


def clear_queue(queue):
    
    #print("Starting to clear the queue")
    
    while True:
        
        b = queue.empty()
    
        if b == 1:
            break
        
        else:
            try:
                i = queue.get_nowait()
            
            except Exception:
                print("Error when clearing the queue.")
                return -1
    
    #print("Finished!")        
    return 1
        

#stager-main
queue_mts = Queue()
queue_stm = Queue()

#client-main
queue_mtc = Queue()
queue_ctm = Queue()