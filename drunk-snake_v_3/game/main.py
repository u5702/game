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


x__x__x_self_ID_x__x__x = 'server#sys'


x = 0
winbitsum = 0
endbit = 0

player_list = []
del player_list[:]


def send_to_all(data, except_player=-1):#
    
    sto = 0
    while sto < x:
        
        if sto == except_player:
            sto += 1
            continue
        
        cm.queue_mts.put((sto, data))
        
        sto += 1
        
        time.sleep(0.2)

       
def remove_player(ID):
    
    bddy = get_from_ID(ID, 3)
    x_b = 0
    for b in player_list:
        
        if b[0] == bddy:
            player_list[x_b] = (b[0], b[1], b[2], '#!sys_none_buddy')
            
        x_b += 1
    
    
    x_i = 0
    for i in player_list:
        
        if i[0] == ID:
            del list[x_i]
            
        x_i += 1


def get_from_ID(ID, l_o):#
    
    for p in player_list:
                    
        if p[0] == ID:
            return p[l_o]
    return -1
    
    
def drink(ID, nmbr):#
        
    name = get_from_ID(ID, 1)
    name.total_schluck += nmbr
    
    if name.buddy != '#!sys_none_buddy':
        
        bID = name.buddy
        bname = get_from_ID(bID, 1)
        bname.total_schluck += nmbr


def spend_guells(playerxx):
    
    
    cm.queue_mts.put((playerxx.socket_id, "sys_action"))
    cm.queue_mts.put((playerxx.socket_id, str(playerxx.guells)))
    cm.clear_queue(cm.queue_stm)

    ts = time.time()                
    while (time.time() - ts) < 15:
                    
        try:
        #if True:
            aw_c_f = cm.queue_stm.get_nowait()
            aw_c = aw_c_f[0]
                            
            if aw_c == 'sys_no':
                break
                                
            elif aw_c == 'sys_yes':
                ldata = ""
                
                mpl = 1       
                while mpl <= x:
        
                    to_add = get_from_ID(mpl, 2)
        
                    if to_add == -1:
                        mpl +=1
                        continue
        
                    ldata = ldata + to_add + " == " + str(mpl) + " | "
        
                    mpl +=1
                                    
                cm.queue_mts.put((playerxx.socket_id, ldata))
                                                
                cm.clear_queue(cm.queue_stm)
                
                tsi = time.time()
                while (time.time() - tsi) < 15:
                                    
                    try:
                    #if True:
                        time.sleep(0.25)
                        aw_c_1_f = cm.queue_stm.get_nowait()
                        time.sleep(0.25)
                        aw_c_2_f = cm.queue_stm.get_nowait()
                        y1 = aw_c_1_f[0]
                        y2 = aw_c_2_f[0]
                        
                        ggt(y1, y2, playerxx)
                        
                        break
                                
                    except Exception:
                        time.sleep(3)
                           
                break
                        
            else:
                break
                
        except Exception:
            time.sleep(3)
                
def ggt(awc1, awc2, playerxx):
    
    cv_1 = awc1[6:]
    cv_2 = awc2[6:]
    aw_c_1 = int(cv_1)
    aw_c_2 = int(cv_2)
                                        
    if aw_c_2 <= playerxx.guells:
                                                
        vname = get_from_ID(aw_c_1, 1)
                                                
        if vname == -1:
            print("error, return -1")
                                                
        else:
            vname.total_schluck += aw_c_2
            playerxx.guells -= aw_c_2
            t_a_data = vname.name + ", trink " + str(aw_c_2) + " Schlücke! (von " + playerxx.name + ")\n"
            send_to_all("sys_info")
            send_to_all(t_a_data)
                                            
    else:
        print("error")

        





x = int(input("Geben Sie die Anzahl an Spielern ein (max. 8): "))


time.sleep(0.25)

print("Starting to connect the clients...\n")

stager.start_stager(4444, x)
stager.start_listener(x, 256)
stager.start_get_from_listener()
stager.start_sender()

print("Done, ", x, " clients are connected")

        
cm.clear_queue(cm.queue_mts)
cm.clear_queue(cm.queue_stm)

send_to_all('name_request')

time.sleep(0.25)

get_name = 1
while get_name <= x:
    
    name_connection = cm.queue_stm.get()
    exec('player{} = game.player(name_connection[0])' .format(get_name))
    exec('player_class_name = player{}' .format(get_name))
    player_class_name.connection = name_connection[1]
    player_list.append((get_name, player_class_name, name_connection[0], player_class_name.buddy))
    
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
                
            number = game.dice()
            dtf = playerxx.dst
                
            if dtf > number:
                playerxx.newlevel(number)
                data1 = playerxx.name +  " hat eine " + str(number) + " gewürfelt und ist jetzt auf Feld " + str(playerxx.level) + "\n"
                fieldnumber = "board/field" + str(playerxx.level) + ".txt"
                a_f = open(fieldnumber, "r")

                for line in a_f:
                    exec('{}' .format(line))
                a_f.close()
                
                send_to_all("sys_info")
                time.sleep(0.15)
                send_to_all(data1)
                time.sleep(0.3)
                
                send_to_all("sys_field")
                time.sleep(0.15)
                send_to_all(str(playerxx.level))
                time.sleep(0.3)
                
                spend_guells(playerxx)
                
                
                
                                  
                    
            elif dtf == number:
                    
                playerxx.newlevel(number)
                data1 = playerxx.name +  "hat gewonnen! --> Alle trinken aus!\n"
                playerxx.winbit = 1
                winbitsum += 1
                
                if winbitsum == (x-1):
                        
                    endbit = 1
                    
                send_to_all("sys_info")
                time.sleep(0.15)
                send_to_all(data1)
                time.sleep(0.3)
                    
                cm.queue_mts.put((playerxx.socket_id, 'sys_won'))
                time.sleep(0.3)
                
                remove_player(i)
                
                    
            else:
                    
                data1 = playerxx.name +  ", ist kurz vor dem Ziel (Feld " + str(playerxx.level) + ") jedoch muss die richtige Zahl gewürfelt werden!\n"
                
                send_to_all("sys_info")
                time.sleep(0.15)
                send_to_all(data1)
                time.sleep(0.3)
                
                spend_guells(playerxx)
                
                    
            playerxx.dist_to_fin(number)
                
        else:
            i += 1
            continue
            
        if endbit == 1:
                
            break
            
        i += 1    
        print("\n")
        #input("###  Drück Enter um fortzufahren  ###")
        print("\n")
            
    if endbit == 1:
                
        il = 1
        while il <= x:
             
            exec('playeryy = player{}' .format(il))
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
                
            exec('send_to_all("Spiel beendet! Der Verlierer ist ", player{}.name, ", der Verlierer Trinkt aus!")' .format(l))
            
        break
            
    print("-------- Neue Runde! -------- \n")