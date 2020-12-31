import copy
import operator
import os
import re
import sys
from functools import reduce

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
tiles = {}

tile = []
n = None
for line in file_data.readlines():
    line = line.replace('\n', '')

    if line == '':
        tiles[n] = tile
        tile = []
        n = None
        continue

    m = re.match(r'^Tile (\d+):$', line)
    if m:
        n = int(m.group(1))
    else:
        tile.append(list(line))

if n and tile:
    tiles[n] = tile

# Get only necessary lines
for k, v in tiles.items():
    ret = []
    ret.append(v[0])
    ret.append(v[-1])

    l = []
    r = []
    for vv in v:
        l.append(vv[0])
        r.append(vv[-1])

    ret.append(l)
    ret.append(r)
    tiles[k] = ret

# Get answer

def flip(tile):
    tb = copy.deepcopy(tile)
    return list(map(lambda x: list(reversed(x)), tb))

def neighbour_tiles(tiles, tile_comp):
    for t1 in tiles:
        for b1 in t1:
            for b2 in tile_comp:
                if b1 == b2:
                    return True

    return False

possible_tiles = {}
for i, tile in tiles.items():
    possible_tiles[i] = set()
    tiles_changed = [tile, flip(tile)]

    for j, tile_comp in tiles.items():
        if i != j and neighbour_tiles(tiles_changed, tile_comp):
            possible_tiles[i].add(j)

corners = []
for i, nt in possible_tiles.items():
    if len(nt) == 2:
        corners.append(i)

answer = reduce(operator.mul, corners, 1)
print(answer)
