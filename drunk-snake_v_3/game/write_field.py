#Autocreate raw fields
#Do not run if there already are fields, they will be overwritten!
import time

print("Start creating the raw fields")

i = 1

while i <= 100:

    exec('f = open("board/field{}.txt", "w")' .format(i))
        
    stw = "Feld" + str(i)    
    
    f.write("#Field\n'print({})'" .format(stw))
    f.close()
    print(i)
    i +=  1

print("Finish")