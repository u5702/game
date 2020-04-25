# Autor: Elijah Grabher
# Date of creation: 13.04.2020
# Last edited: 15.04.2020
import time
import game_classes as game
import board
import stager
import threading
from queue import Queue
import communication_manager as cm


x = 0
winbitsum = 0
endbit = 0

x = int(input("Geben Sie die Anzahl an Spielern ein (max. 8): "))

time.sleep(0.25)

print("Starting to connect the clients...\n")

stager.start_stager(4444, x)
stager.start_listener(x, 256)
stager.start_get_from_listener()
stager.start_sender()

print("Done, ", x, " clients are connected")


def send_to_all(data, except_player=-1):
    
    sto = 0
    while sto < x:
        
        if sto == except_player:
            sto += 1
            continue
        
        cm.queue_mts.put((sto, data))
        
        sto += 1
        
        time.sleep(0.2)
        
        
send_to_all('name_request')

time.sleep(0.25)

get_name = 1
while get_name <= x:
    
    name_connection = cm.queue_stm.get()
    exec('player{} = game.player(name_connection[0])' .format(get_name))
    exec('player_class_name = player{}' .format(get_name))
    player_class_name.connection = name_connection[1]
    
    j = 0
    while j < x:
        
        if stager.connection_list[j] == name_connection[1]:
            player_class_name.socket_id = j
        j += 1
    
    get_name += 1


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
        
        exec('playerxx = player{}' .format(i))
        winbit = playerxx.winbit
        if winbit == 0:
                
            number = 1#game.dice()
            dtf = playerxx.dst
                
            if dtf > number:
                playerxx.newlevel(number)
                data1 = playerxx.name +  " hat eine " + str(number) + " gewürfelt und ist jetzt auf Feld " + str(playerxx.level)
                send_to_all(data1)
                fieldnumber = "board/field" + str(playerxx.level) + ".txt"
                a_f = open(fieldnumber, "r")

                for line in a_f:
                    exec('{}' .format(line))
                a_f.close()
                
                cm.queue_mts.put((playerxx.socket_id, str(i)))
                time.sleep(0.2)
                
                send_to_all(data1, playerxx.socket_id)
                  
                    
            elif dtf == number:
                    
                playerxx.newlevel(number)
                data1 = playerxx.name +  "hat gewonnen! --> Alle trinken aus!"
                playerxx.winbit = 1
                winbitsum += 1
                
                if winbitsum == (x-1):
                        
                    endbit = 1
                    
                cm.queue_mts.put((playerxx.socket_id, 'sys_won'))
                time.sleep(0.2)
                
                send_to_all(data1)
                    
            else:
                    
                data1 = playerxx.name +  ", ist kurz vor dem Ziel (Feld " + str(playerxx.level) + ") jedoch muss die richtige Zahl gewürfelt werden!"
                cm.queue_mts.put((playerxx.socket_id, 'sys_rnmbr'))
                time.sleep(0.2)
                
                send_to_all(data1)
                
                    
            playerxx.dist_to_fin(number)
                
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
             
            playeryy = "player" + str(il)
            winbit = playeryy.winbit
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