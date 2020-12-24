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

max_v = max(cups) + 1
while max_v <= 1000000:
    cups.append(max_v)
    max_v += 1

# Get answer
move = 0
moves = 10000000
l = len(cups)
cur = cups[0]
cups = {c: cups[(i + 1) % l] for i, c in enumerate(cups)}

while move < moves:
    sel_1 = cups[cur]
    sel_2 = cups[sel_1]
    sel_3 = cups[sel_2]

    dest = cur - 1
    dest = l if dest == 0 else dest
    while dest == sel_1 or dest == sel_2 or dest == sel_3:
        dest -= 1
        dest = l if dest == 0 else dest

    cups[cur] = cups[sel_3]
    cups[sel_3] = cups[dest]
    cups[dest] = sel_1
    cur = cups[cur]
    move += 1

v1 = cups[1]
v2 = cups[v1]
answer = v1 * v2
print(answer)
