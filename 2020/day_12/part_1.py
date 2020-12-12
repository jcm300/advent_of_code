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
    'D': 'E', # Direction
}

def rotate(sd, d, v):
    dirs = ['N', 'E', 'S', 'W']
    i = dirs.index(sd)

    while v >= 360:
        v -= 360

    v = v / 90
    i = i + v if d == 'R' else i - v
    i = i % 4
    return dirs[int(i)]

def move_to(pos, d, v):
    if d == 'N':
        pos['N'] += v
    elif d == 'S':
        pos['N'] -= v
    elif d == 'E':
        pos['E'] += v
    elif d == 'W':
        pos['E'] -= v

for move in moves:
    if move['m'] == 'F':
        move_to(pos, pos['D'], move['v'])
    elif move['m'] in ['N', 'S', 'E', 'W']:
        move_to(pos, move['m'], move['v'])
    elif move['m'] in ['R', 'L']:
        pos['D'] = rotate(pos['D'], move['m'], move['v'])

answer = abs(pos['N']) + abs(pos['E'])
print(answer)
