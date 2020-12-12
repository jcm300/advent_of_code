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
layout = []

for line in file_data.readlines():
    line = line.replace('\n', '')
    
    layout.append(list(line))

# Get answer

def get_first(layout, i, j, d_i, d_j, y_len, x_len):
    while 0 <= i + d_i < y_len and 0 <= j + d_j < x_len:
        i += d_i
        j += d_j

        if layout[i][j] != '.':
            break

    return layout[i][j]

def adjacent_first_occupied(layout, i, j, y_len, x_len):
    n = 0

    if i - 1 >= 0:
        if get_first(layout, i, j, -1, 0, y_len, x_len) == '#':
            n += 1

        if j - 1 >= 0 and get_first(layout, i, j, -1, -1, y_len, x_len) == '#':
            n += 1

    if i + 1 < y_len:
        if get_first(layout, i, j, 1, 0, y_len, x_len) == '#':
            n += 1

        if j + 1 < x_len and get_first(layout, i, j, 1, 1, y_len, x_len) == '#':
            n += 1

    if j - 1 >= 0:
        if get_first(layout, i, j, 0, -1, y_len, x_len) == '#':
            n += 1

        if i + 1 < y_len and get_first(layout, i, j, 1, -1, y_len, x_len) == '#':
            n += 1

    if j + 1 < x_len:
        if get_first(layout, i, j, 0, 1, y_len, x_len) == '#':
            n += 1

        if i - 1 >= 0 and get_first(layout, i, j, -1, 1, y_len, x_len) == '#':
            n += 1

    return n

def seat_people(layout):
    i = 0
    y_len = len(layout)
    x_len = len(layout[0]) # can explode
    n_seated = 0
    new_layout = []

    while i < y_len:
        j = 0
        new_layout.append([])

        while j < x_len:
            adj = adjacent_first_occupied(layout, i, j, y_len, x_len)

            if layout[i][j] == 'L' and adj == 0:
                new_layout[i].append('#')
            elif layout[i][j] == '#' and adj > 4:
                new_layout[i].append('L')
            else:
                new_layout[i].append(layout[i][j])

            if new_layout[i][j] == '#':
                n_seated += 1

            j += 1
        i += 1

    return new_layout, n_seated

n_seated = 0
layout, new_n_seated = seat_people(layout)

while n_seated != new_n_seated:
    n_seated = new_n_seated
    layout, new_n_seated = seat_people(layout)

print(n_seated)
