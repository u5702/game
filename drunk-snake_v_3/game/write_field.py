#Autocreate raw fields
#Do not run if there already are fields, they will be overwritten!
import time

print("Start creating the raw fields")

i = 1

while i <= 100:

    exec('f = open("board_client/field{}.txt", "w")' .format(i))   
    
    f.write('Feld{}' .format(i))
    f.close()
    print(i)
    i +=  1

print("Finish")