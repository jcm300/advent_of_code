import copy
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
tiles = []
for line in file_data.readlines():
    line = line.replace('\n', '')

    line = re.sub(r'(e|w|se|sw|nw|ne)', r'\1|', line)
    dirs = line.split('|')
    dirs.remove('')
    tiles.append(dirs)

# Get answer
pos = [{'e': 0, 'w': 0, 'se': 0, 'sw': 0, 'nw': 0, 'ne': 0} for i in range(len(tiles))]

for i, t in enumerate(tiles):
    for m in t:
        pos[i][m] += 1

pos_p = []
for p in pos:
    # Remove unecessary moves
    se = p['se'] - p['nw']
    ne = p['ne'] - p['sw']
    e = p['e'] - p['w']

    # Transform to only two coords
    x = e
    y = se

    x += ne
    y -= ne

    pos_p.append({
        'x': x,
        'y': y,
    })

counts = {}
for p in pos_p:
    t = f'{p["x"]}|{p["y"]}'

    if t in counts:
        counts[t] += 1
    else:
        counts[t] = 1

tiles = []
for c in counts:
    b = counts[c] % 2 != 0
    if b:
        coords = c.split('|')
        tiles.append({
            'x': int(coords[0]),
            'y': int(coords[1]),
            'b': b,
        })

def in_tiles(x, y, tiles):
    for t in tiles:
        if x == t['x'] and y == t['y']:
            return t

    return None

def adj_black(x, y, tiles, new_tiles, create):
    ret = 0

    t = in_tiles(x, y, tiles)
    if t:
        ret = 1 if t['b'] else 0
    
    if create:
        t = {'x': x, 'y': y, 'b': False}
        new_tiles = adj_blacks(t, tiles, new_tiles)

    return ret, new_tiles

def adj_blacks(tile, tiles, new_tiles):
    adjs = 0

    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]:
        a, new_tiles = adj_black(tile['x'] + x, tile['y'] + y, tiles, new_tiles, tile['b'])
        adjs += a

    nt = copy.deepcopy(tile)
    if (tile['b'] and (adjs == 0 or adjs > 2)) or (not tile['b'] and adjs == 2):
        nt['b'] = not tile['b']

    if nt['b'] and nt not in new_tiles:
        new_tiles.append(nt)

    return new_tiles

days = 100
day = 0
# A bit slow, need some performance optimizations
while day < days:
    new_tiles = []
    for t in tiles:
        new_tiles = adj_blacks(t, tiles, new_tiles) 
        
    day += 1
    tiles = new_tiles

answer = len(tiles)
print(answer)
