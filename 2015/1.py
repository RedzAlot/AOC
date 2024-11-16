from utils import *

directions = read_file_2_string("1.txt")
print(len(directions))
print(directions)
floor = 0
i = 1

for c in directions:
    if c == "(":
        floor+=1
    else:
        floor-=1
    if floor==-1:
        print("hit basement at " + str(i))
        break
    i+=1
        

print(floor)