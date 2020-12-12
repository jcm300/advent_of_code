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
moves = []

for line in file_data.readlines():
    line = line.replace('\n', '')
    
    parts = re.search(r'^(\w)(\d+)$', line)
    moves.append({'m': parts.group(1), 'v': int(parts.group(2))})

# Get answer
pos = {
    'N': 0, # > 0 North, < 0 South
    'E': 0, # > 0 East, < 0 West
}

way = {
    'N': 1, # > 0 North, < 0 South
    'E': 10, # > 0 East, < 0 West
}

def rotate(way, d, v):
    ns = way['N'] > 0
    ew = way['E'] > 0

    while v >= 360:
        v -= 360

    v = v / 90

    if v == 2:
        way['N'] = -way['N']
        way['E'] = -way['E']
    elif (d == 'R' and v == 1) or (d == 'L' and v == 3):
        aux = way['E']
        way['E'] = way['N']
        way['N'] = -aux
    elif (d == 'R' and v == 3) or (d == 'L' and v == 1):
        aux = way['E']
        way['E'] = -way['N']
        way['N'] = aux

def move_to(way, d, v):
    if d == 'N':
        way['N'] += v
    elif d == 'S':
        way['N'] -= v
    elif d == 'E':
        way['E'] += v
    elif d == 'W':
        way['E'] -= v

for move in moves:
    if move['m'] == 'F':
        pos['N'] += move['v'] * way['N']
        pos['E'] += move['v'] * way['E']
    elif move['m'] in ['N', 'S', 'E', 'W']:
        move_to(way, move['m'], move['v'])
    elif move['m'] in ['R', 'L']:
        rotate(way, move['m'], move['v'])

answer = abs(pos['N']) + abs(pos['E'])
print(answer)
