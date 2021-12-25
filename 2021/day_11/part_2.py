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
    matrix.append([[int(v), False] for v in l])

#
# Get answer
#
y_len = len(matrix)
x_len = len(matrix[0])

def flash(matrix, x, y):
    if matrix[y][x][0] > 9 and not matrix[y][x][1]:
        # Mark as flashed
        matrix[y][x][1] = True

        # Look to adjacent ones
        if x-1 >= 0:
            matrix[y][x-1][0] += 1
            matrix = flash(matrix, x-1, y)

            if y-1 >= 0:
                matrix[y-1][x-1][0] += 1
                matrix = flash(matrix, x-1, y-1)

            if y+1 < y_len:
                matrix[y+1][x-1][0] += 1
                matrix = flash(matrix, x-1, y+1)

        if x+1 < x_len:
            matrix[y][x+1][0] += 1
            matrix = flash(matrix, x+1, y)

            if y-1 >= 0:
                matrix[y-1][x+1][0] += 1
                matrix = flash(matrix, x+1, y-1)

            if y+1 < y_len:
                matrix[y+1][x+1][0] += 1
                matrix = flash(matrix, x+1, y+1)

        if y-1 >= 0:
            matrix[y-1][x][0] += 1
            matrix = flash(matrix, x, y-1)

        if y+1 < y_len:
            matrix[y+1][x][0] += 1
            matrix = flash(matrix, x, y+1)

    return matrix

def step(matrix):
    # Increase 1
    for y in range(y_len):
        for x in range(x_len):
            matrix[y][x][0] += 1

    # Flashes
    for y in range(y_len):
        for x in range(x_len):
            matrix = flash(matrix, x, y)

    # Reset Flashes
    for y in range(y_len):
        for x in range(x_len):
            if matrix[y][x][0] > 9:
                matrix[y][x][0] = 0
                matrix[y][x][1] = False

    return matrix

def check_sync(matrix):
    value_to_check = matrix[0][0]

    for y in range(y_len):
        for x in range(x_len):
            if value_to_check != matrix[y][x]:
                return False

    return True

answer = 0
sync = False

while not sync:
    matrix = step(matrix)
    sync = check_sync(matrix)
    answer += 1

print(answer)
