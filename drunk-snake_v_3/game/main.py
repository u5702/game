# Autor: Elijah Grabher
# Date of creation: 13.04.2020
# Last edited: 15.04.2020
#D pipe hurat...
import time
import socket
import multiprocessing
import game_classes as game
import board
import stager

mts = multiprocessing.Queue()
stm = multiprocessing.Queue()

x = 0
winbitsum = 0
endbit = 0

f_user = open("config/user_config.txt", "r")

for line in f_user:
        
    exec('{}' .format(line))

f_user.close()

c = 1
while c <= 8:
    
    exec('name = nm{}' .format(c))
    
    if name == "":
        c += 1
        continue
    
    else:
        exec('player{} = game.player(nm{})' .format(c, c))
        exec('print(player{}.name, "ist dabei!")' .format(c))
        c += 1
        x += 1

stgr_process = multiprocessing.process(target=stgr, args=(mts, stm ,x))
stgr_process.start()

while True:
    
    if stager.con_set == 1:
        break
    

print("\n")
f_snake = open("art/art_snake.txt", "r")

for line in f_snake:
        
    print(line)

f_snake.close()
print("\n")
print("Los geht's mit drunk-snake!\n")
input(">>>>>>>>Enter drücken um zu starten!<<<<<<<<\n")
    

while True:
        
    i = 1
    while i <= x:
            
        exec('winbit = player{}.winbit' .format(i))
        if winbit == 0:
                
            number = game.dice()
            exec('dtf = player{}.dst' .format(i))
                
            if dtf > number:
                exec('player{}.newlevel(number)' .format(i))
                exec('print(player{}.name ,  "hat eine ", number, " gewürfelt und ist jetzt auf Feld ", player{}.level)' .format(i, i))
                exec('print("Feld ", player{}.level, ":")' .format(i))
                exec('fieldnumber = player{}.level' .format(i))
                exec('a_f = board.field{}.action' .format(fieldnumber))
                f_a_f = open(a_f, "r")
                for line in f_a_f:
                    exec('{}' .format(line))
                f_a_f.close()
                    
                    
            elif dtf == number:
                    
                exec('player{}.newlevel(number)' .format(i))
                exec('print(player{}.name ,  "hat gewonnen! --> Alle trinken aus!")' .format(i))
                exec('player{}.winbit = 1' .format(i))
                winbitsum += 1
                if winbitsum == (x-1):
                        
                    endbit = 1
                    
            else:
                    
                exec('print(player{}.name ,  ", ist kurz vor dem Ziel (Feld ", player{}.level , ") jedoch muss die richtige Zahl gewürfelt werden!")' .format(i, i))
                    
            exec('player{}.dist_to_fin({})' .format(i, number))
                
        else:
            i += 1
            continue
            
        if endbit == 1:
                
            break
            
        i += 1    
        print("\n")
        input("###  Drück Enter um fortzufahren  ###")
            print("\n")
            
    if endbit == 1:
                
        il = 1
        while il <= x:
                    
            exec('winbit = player{}.winbit' .format(il))
            if winbit == 1:
                        
                il += 1
                    
            else:
                        
                l = il
                break
        if il == 0:
                
            print("Error")
            break
            
        else:
                
            exec('print("Spiel beendet! Der Verlierer ist ", player{}.name, ", der Verlierer Trinkt aus!")' .format(l))
            
        break
            
    print("-------- Neue Runde! -------- \n")