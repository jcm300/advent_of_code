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
x_points = []
y_points = []
folds = []

for line in file_data.readlines():
    l = line.replace('\n', '')

    if ',' in l:
        x, y = l.split(',')
        x_points.append(int(x))
        y_points.append(int(y))
    
    elif 'fold along' in l:
        l = l.replace('fold along ', '')
        d, v = l.split('=')
        folds.append({'dir': d, 'value': int(v)})

# Build matrix
x_len = max(x_points) + 1
y_len = max(y_points) + 1

matrix = []
for y in range(y_len):
    matrix.append([0] * x_len)

for x, y in zip(x_points, y_points):
    matrix[y][x] = 1

#
# Get answer
#

def fold_y(matrix, y):
    y_l = len(matrix)
    x_l = len(matrix[0])
    m = []

    # Copy the half up to the new matrix
    for i in range(y):
        m.append(matrix[i])

    # Merge half down with the half up
    for i, y_p in enumerate(range(y+1, y_l)):
        y_n = y_p - ((i+1)*2)

        for x in range(x_l):
            m[y_n][x] = m[y_n][x] or matrix[y_p][x]

    return m

def fold_x(matrix, x):
    y_l = len(matrix)
    x_l = len(matrix[0])
    m = []

    # Copy the left part to the new matrix
    for y in range(y_l):
        m.append(matrix[y][:x])

    # Merge right part with the left part
    for y in range(y_l):
        for i, x_p in enumerate(range(x+1, x_l)):
            x_n = x_p - ((i+1)*2)
            m[y][x_n] = m[y][x_n] or matrix[y][x_p]

    return m

# Do the folds
for fold in folds:
    if fold['dir'] == 'y':
        matrix = fold_y(matrix, fold['value'])

    elif fold['dir'] == 'x':
        matrix = fold_x(matrix, fold['value'])

# Print matrix to see the answer
for y in range(len(matrix)):
    print(''.join(map(lambda c: '1' if c else ' ', matrix[y])))
