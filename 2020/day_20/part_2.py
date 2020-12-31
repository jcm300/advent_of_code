import copy
import math
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

# Get answer

def get_borders(tile):
    ret = []
    ret.append(tile[0])
    ret.append(tile[-1])

    l = []
    r = []
    for vv in tile:
        l.append(vv[0])
        r.append(vv[-1])

    ret.append(l)
    ret.append(r)

    return ret

def flip(tile):
    tb = copy.deepcopy(tile)
    return list(map(lambda x: list(reversed(x)), tb))

def rotate_right(tile):
    ret = rotate_left(tile)
    ret = rotate_left(ret)
    ret = rotate_left(ret)
    return ret

def rotate_180(tile):
    ret = rotate_left(tile)
    ret = rotate_left(ret)
    return ret

def rotate_left(tile):
    tile = copy.deepcopy(tile)
    return [[tile[j][i] for j in range(len(tile))] for i in range(len(tile[0])-1,-1,-1)]

def neighbour_tiles(t1, i, tiles, notin=[]):
    ret = []
    tb1 = get_borders(t1)

    for j in tiles.keys():
        if i != j and j not in notin:
            for r, f, t in combs[j]:
                tb2 = get_borders(t)

                if tb1[0] == tb2[1]:
                    ret.append({'d': 'u', 't': j, 'r': r, 'f': f, 'tl': t})
                    break
                elif tb1[1] == tb2[0]:
                    ret.append({'d': 'd', 't': j, 'r': r, 'f': f, 'tl': t})
                    break
                elif tb1[2] == tb2[3]:
                    ret.append({'d': 'l', 't': j, 'r': r, 'f': f, 'tl': t})
                    break
                elif tb1[3] == tb2[2]:
                    ret.append({'d': 'r', 't': j, 'r': r, 'f': f, 'tl': t})
                    break

    return ret

# Convert grid to str without borders
def str_img(grid):
    lg = len(grid)
    lb = len(grid[0][0][0]) - 2 # minus first and last line
    l = lg * lb

    aux = [[] for j in range(l)]
    for i in range(lg):
        for j in range(lg):
            for w in range(lb):
                aux[i*lb + w] += grid[i][j][w+1][1:-1] # +1 ignores first line, and ignore first and last value of each line

    str_img = ''

    for a in aux:
        str_img += ''.join(a) + '\n'

    return str_img

# Calc combinations
combs = {}
for i, tile in tiles.items():
    flip_tile = flip(tile)
    combs[i] = [(0, False, copy.deepcopy(tile)),
                (90, False, rotate_left(tile)),
                (180, False, rotate_180(tile)),
                (270, False, rotate_right(tile)),
                (0, True, flip_tile),
                (90, True, rotate_left(flip_tile)),
                (180, True, rotate_180(flip_tile)),
                (270, True, rotate_right(flip_tile))]

# Find neightbour tiles
possible_tiles = {}
for i, tile in tiles.items():
    possible_tiles[i] = neighbour_tiles(tile, i, tiles)

# Init grids
l = int(math.sqrt(len(tiles)))
grid = [[None for i in range(l)] for j in range(l)]
grid_ids = [[None for i in range(l)] for j in range(l)]

# Find top left corner
for pt in possible_tiles:
    ts = possible_tiles[pt]
    if len(ts) == 2 and ts[0]['d'] in ['d', 'r'] and ts[1]['d'] in ['d', 'r']:
        grid[0][0] = tiles[pt]
        grid_ids[0][0] = pt
        break

# Build image
for i in range(l):
    for j in range(l):
        if grid_ids[i][j] is not None:
            notin = [item for sl in grid_ids for item in sl]
            nt = neighbour_tiles(grid[i][j], grid_ids[i][j], tiles, notin)

            for pt in nt:
                if pt['d'] == 'r' and j + 1 < l:
                    grid_ids[i][j+1] = pt['t']
                    grid[i][j+1] = pt['tl']
                elif pt['d'] == 'd' and i + 1 < l:
                    grid_ids[i+1][j] = pt['t']
                    grid[i+1][j] = pt['tl']

str_image = str_img(grid)
