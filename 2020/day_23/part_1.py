import os
import re
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
line = file_data.readline()
line = line.replace('\n', '')
cups = list(map(lambda x: int(x), line))

# Get answer
move = 0
moves = 100

while move < moves:
    sel_cups = cups[1:4]
    del cups[1:4]

    dest_cup = cups[0] - 1
    dest_cup = 9 if dest_cup == 0 else dest_cup
    while dest_cup in sel_cups:
        dest_cup -= 1
        dest_cup = 9 if dest_cup == 0 else dest_cup
    
    dest_ind = cups.index(dest_cup)
    cups = cups[1:dest_ind+1] + sel_cups + cups[dest_ind+1:] + [cups[0]]
    move += 1

one_ind = cups.index(1)
answer = ''.join(map(str, cups[one_ind+1:] + cups[:one_ind]))
print(answer)
