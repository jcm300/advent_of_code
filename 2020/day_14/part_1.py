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
masks = []
lines = file_data.readlines()
mask = {'mask': lines[0].replace('\n', '').split(' = ')[1], 'writes': []}

for line in lines[1:]:
    line = line.replace('\n', '')
    parts = line.split(' = ')
    
    if parts[0] == 'mask':
        masks.append(mask)
        mask = {'mask': parts[1], 'writes': []}
    else:
        match = re.search(r'^mem\[(\d+)\] = (\d+)$', line)
        mask['writes'].append({
            'p': int(match.group(1)),
            'v': int(match.group(2)),
        })

masks.append(mask)

# Get answer
bits = 36
mem = {}

def int2bin(n):
    b = ''

    while n > 0:
        n, bn = divmod(n, 2)
        b = str(bn) + b

    return b.zfill(bits)

def bitmask(v, mask):
    r = ''

    for i, m in enumerate(mask):
        if m == 'X':
            r += v[i]
        else:
            r += m

    return r

for m in masks:
    for write in m['writes']:
        mem[write['p']] = int(bitmask(int2bin(write['v']), m['mask']), 2)

answer = sum(mem.values())
print(answer)
