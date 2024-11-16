from utils import *

# Santa by himself

x, y = 0, 0

directions = read_file_2_string("3.txt")

visited_coordinates = set()
visited_coordinates.add((x, y))

# adding new cords
for direction in directions:
    if direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    elif direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    # Add new coordinates to the set and does not add if is already in the set - python logic
    visited_coordinates.add((x, y))
   
# finished
print("Part one:")
# print("unique cords:", visited_coordinates)
print("num unique houses:", len(visited_coordinates))
print(" ")

# Santa and robot
x, y = 0, 0
x_o, y_o = 0, 0
visited = set()
visited.add((x, y))

i=0
for direction in directions:
    is_even = i % 2 == 0
    if is_even:
        #santa
        if direction == "<":
            x -= 1
        elif direction == ">":
            x += 1
        elif direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        visited.add((x, y))
    else:
        # robot
        if direction == "<":
            x_o -= 1
        elif direction == ">":
            x_o += 1
        elif direction == "^":
            y_o += 1
        elif direction == "v":
            y_o -= 1
        visited.add((x_o, y_o))

    i+=1
# Finished
print("Part two:")
# print("unique cords visited with both robot and santa:", visited_coordinates)
print("num unique visited houses with both robot and santa:", len(visited))   
print("total directions in file:", count_characters_in_file("3.txt"))
