import os
import re
import sys
import math

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

#
# Parse file
#
vertices = set()
lines = []

for line in file_data.readlines():
    l = line.replace('\n', '')
    p1, p2 = l.split('-')

    vertices.add(p1)
    vertices.add(p2)
    lines.append({'p1': p1, 'p2': p2})

connections = {}

for v in vertices:
    connections[v] = set()

for line in lines:
    p1 = line['p1']
    p2 = line['p2']

    connections[p1].add(p2)
    connections[p2].add(p1)

#
# Get answer
#
paths = []

def try_path(connections, conn, path, small_used):
    paths = []
    path += ',' + conn
    
    if conn == 'end':
        paths.append(path)

    else:
        for c in connections[conn]:
            if c.upper() == c or c not in path or (not small_used and c != 'start'):
                su = small_used or (c.upper() != c and path.count(c) + 1 == 2)
                ps = try_path(connections, c, path, su)
                paths += ps

    return paths

for conn in connections['start']:
    ps = try_path(connections, conn, 'start', False)
    paths += ps

answer = len(paths)
print(answer)
