import os
import re
import sys
from functools import reduce
import operator

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
    matrix.append(list(map(int, l)))

#
# Get answer
#
basins_sizes = []
y_len = len(matrix)
x_len = len(matrix[0])

def get_basins_size(matrix, x, y, passed):
    ret = 1
    passed.append((x, y))

    if (x-1, y) not in passed and x-1 >= 0 and matrix[y][x-1] != 9:
        ret += get_basins_size(matrix, x-1, y, passed)

    if (x+1, y) not in passed and x+1 < x_len and matrix[y][x+1] != 9:
        ret += get_basins_size(matrix, x+1, y, passed)

    if (x, y-1) not in passed and y-1 >= 0 and matrix[y-1][x] != 9:
        ret += get_basins_size(matrix, x, y-1, passed)

    if (x, y+1) not in passed and y+1 < y_len and matrix[y+1][x] != 9:
        ret += get_basins_size(matrix, x, y+1, passed)

    return ret

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

        ret = get_basins_size(matrix, x, y, []) 
        basins_sizes.append(ret)

sorted_sizes = sorted(basins_sizes)
answer = reduce(operator.mul, sorted_sizes[-3:], 1)
print(answer)
