import os
import re
import sys

# Read arguments
if len(sys.argv) != 4:
    raise ValueError('Please provide a filename input and slope direction (right, down)')

filename = sys.argv[1]
right = int(sys.argv[2])
down = int(sys.argv[3])
pos = {
    'right': 0,
    'down': 0,
}

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
map_matrix = []

for line in file_data.readlines():
    row = []
    line = line.replace('\n', '')

    for char in line:
        row.append(1 if char == '#' else 0)

    map_matrix.append(row)

# Get answer
found_trees = 0
hei_len = len(map_matrix)
hor_len = len(map_matrix[0])

while pos['down'] < hei_len:
    pos['right'] += right
    pos['down'] += down
    
    # Outside map
    if pos['right'] >= hor_len:
        pos['right'] -= hor_len

    # Outside map
    if pos['down'] >= hei_len:
        break

    if map_matrix[pos['down']][pos['right']]:
        found_trees += 1
    
print(found_trees)
