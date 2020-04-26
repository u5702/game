# Autor: Elijah Grabher
# Date of creation: 13.04.2020
# Last edited: 15.04.2020

#start
import time
import random

#Classes
class player:
    
    def __init__(self, nm, bddy='#!sys_none_buddy'):
        
        self.name = nm
        self.connection = ()
        self.socket_id = -1
        self.level = 0
        self.dst = 100
        self.winbit = 0
        self.buddy = bddy
        self.pupi = 0
        self.guells = 0
        self.total_schluck = 0
        self.total_ex = 0
        
    def newlevel(self, lvl):
        
        self.level += lvl
    
    def dist_to_fin(self, nmbr):
    
        self.dst = (100 - self.level)
        
    def add_buddy(self, ID):
        
        self.buddy = ID

class field:
    
    def __init__(self, id):
        
        self.id = 0
        self.action = ''

    def f_action(self, act):
        
        self.action = act
    
#Functions  
def dice():
    
    result = random.randint(1, 6)
    return result


#end