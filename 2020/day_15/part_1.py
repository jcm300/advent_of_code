import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
line = file_data.readline()
numbers = {int(n):{'tf': None, 'tl': i+1} for i, n in enumerate(line.split(','))}

# Get answer

def get_replace(numbers, n, i):
    nn = numbers.get(n)

    if nn:
        del numbers[n]
        nn['tf'] = nn['tl']
    else:
        nn = {'tf': None}

    nn['tl'] = i+1
    numbers[n] = nn

i = len(numbers)
th = 2020

while i < th:
    last = list(numbers)[-1]

    if numbers[last]['tf'] is None:
        get_replace(numbers, 0, i)
    else:
        nb = numbers[last]
        n = nb['tl'] - nb['tf']
        get_replace(numbers, n, i)

    i += 1

answer = list(numbers)[-1]
print(answer)
