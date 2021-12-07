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

    if x1 == x2 or y1 == y2:
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

    if x1 == x2:
        d = abs(y1 - y2) + 1
        sign = 1 if y1 < y2 else -1

        for y in range(d):
            matrix[y1 + sign*y][x1] += 1

    elif y1 == y2:
        d = abs(x1 - x2) + 1
        sign = 1 if x1 < x2 else -1

        for x in range(d):
            matrix[y1][x1 + sign*x] += 1

# Calculate answer
answer = 0

for y in matrix:
    for x in y:
        if x >= 2:
            answer += 1

print(answer)
