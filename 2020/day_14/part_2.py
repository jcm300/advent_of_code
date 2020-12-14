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
        if m == '0':
            r += v[i]
        else:
            r += m

    return r

def all_addr(f_bin):
    addrs = [f_bin]
    i = 0
    
    while i < bits:
        aux_l = []
        for addr in addrs:
            while i < bits and addr[i] != 'X':
                i += 1

            if i < bits:
                aux = list(addr)
                aux[i] = '0'
                aux_l.append(''.join(aux))
                aux[i] = '1'
                aux_l.append(''.join(aux))
            else:
                break
        else:
            addrs = aux_l
            i += 1

    return list(map(lambda k: int(k, 2), addrs))

for m in masks:
    for write in m['writes']:
        bp = bitmask(int2bin(write['p']), m['mask'])
        addrs = all_addr(bp)

        for addr in addrs:
            mem[addr] = write['v']

answer = sum(mem.values())
print(answer)
