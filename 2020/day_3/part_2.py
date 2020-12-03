import operator
import os
import re
import sys
from functools import reduce

# Read arguments
if len(sys.argv) != 3:
    raise ValueError('Please provide a filename input and the slope file')

filename = sys.argv[1]
slope_filename = sys.argv[2]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')
slope_file_data = open(os.getcwd() + '/' + slope_filename, 'r')

# Parse files
map_matrix = []

for line in file_data.readlines():
    row = []
    line = line.replace('\n', '')

    for char in line:
        row.append(1 if char == '#' else 0)

    map_matrix.append(row)

slopes = []

for line in slope_file_data.readlines():
    slope = {}  
    line = line.replace('\n', '')
    dirs = line.split(' ')
    
    slope['right'] = int(dirs[0])
    slope['down'] = int(dirs[1])

    slopes.append(slope)

# Get answer
def traverse(map_matrix, slope):
    found_trees = 0
    pos = {
        'right': 0,
        'down': 0,
    }
    hei_len = len(map_matrix)
    hor_len = len(map_matrix[0])

    while pos['down'] < hei_len:
        pos['right'] += slope['right']
        pos['down'] += slope['down']
        
        # Outside map
        if pos['right'] >= hor_len:
            pos['right'] -= hor_len

        # Outside map
        if pos['down'] >= hei_len:
            break

        if map_matrix[pos['down']][pos['right']]:
            found_trees += 1

    return found_trees
    
found_trees = []

for slope in slopes:
    found_trees.append(traverse(map_matrix, slope))

found_trees = reduce(operator.mul, found_trees)
print(found_trees)
