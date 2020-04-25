import time
from queue import Queue
import threading
import communication_manager as cm
import stager


stager.start_stager(4444, 2)
stager.start_listener(2, 256)
stager.start_get_from_listener()
stager.start_sender()


cm.queue_mts.put((0, "to socket 0 -- message 0\n"))
cm.queue_mts.put((0, "to socket 1 -- message 0\n"))
cm.queue_mts.put((0, "to socket 0 -- message 1\n"))
cm.queue_mts.put((0, "to socket 1 -- message 1\n"))


while True:
    
    print(cm.queue_stm.get())


