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

answer = 0
for c in counts:
    if counts[c] % 2 != 0:
        answer += 1
print(answer)
