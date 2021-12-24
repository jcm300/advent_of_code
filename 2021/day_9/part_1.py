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
matrix = []

for line in file_data.readlines():
    l = line.replace('\n', '')
    matrix.append(list(l))

#
# Get answer
#
answer = 0
y_len = len(matrix)
x_len = len(matrix[0])

for y in range(y_len):
    for x in range(x_len):
        v = matrix[y][x]

        if x-1 >= 0 and v >= matrix[y][x-1]:
            continue
        if x+1 < x_len and v >= matrix[y][x+1]:
            continue
        if y-1 >= 0 and v >= matrix[y-1][x]:
            continue
        if y+1 < y_len and v >= matrix[y+1][x]:
            continue

        answer += int(v) + 1

print(answer)
