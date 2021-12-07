import os
import re
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

#
# Parse file
#
lines = []
max_x = 0
max_y = 0

for line in file_data.readlines():
    l = line.replace('\n', '')
    pos_1, pos_2 = l.split(' -> ')

    x1, y1 = map(int, pos_1.split(','))
    x2, y2 = map(int, pos_2.split(','))

    max_x = max(x1, x2, max_x)
    max_y = max(y1, y2, max_y)

    lines.append([x1, y1, x2, y2])

#
# Get answer
#

# Build diagram
matrix = []
max_x += 1
max_y += 1

for y in range(max_y):
    matrix.append([0] * max_x)

# Fill diagram
for line in lines:
    x1, y1, x2, y2 = line

    dy = abs(y1 - y2) + 1
    dx = abs(x1 - x2) + 1
    sign_y = 1 if y1 < y2 else -1
    sign_x = 1 if x1 < x2 else -1

    if dy == dx:
        rx = ry = range(dx)
    elif dy > dx:
        ry = range(dy)
        rx = [0] * dy
    else:
        rx = range(dx)
        ry = [0] * dx

    for y, x in zip(ry, rx):
        matrix[y1 + sign_y*y][x1 + sign_x*x] += 1

# Calculate answer
answer = 0

for y in matrix:
    for x in y:
        if x >= 2:
            answer += 1

print(answer)
