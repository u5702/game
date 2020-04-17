#Autocreate raw board
import time

print("Start creating the raw Board")

i = 1

f = open("board_raw.py", "w")

f.write("#Board\n")
f.write("import time\nimport game_classes as game\n\n#Start\n\n\n")


while i <= 100:
     
     f.write("#Field_{}\nfield{} = game.field({})\nfield{}.f_action('board/field{}.txt') \n" .format(i, i, i, i, i))
     time.sleep(0.05)
     
     i += 1
     
f.write("#End")
     
f.close()

print("Finish")