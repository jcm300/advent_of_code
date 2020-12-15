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
# A bit slow, need to be improved

def get_replace(numbers, n, i):
    nn = numbers.get(n)

    if nn:
        nn['tf'] = nn['tl']
    else:
        nn = {'tf': None}

    nn['tl'] = i+1
    numbers[n] = nn
    return nn

i = len(numbers)
th = 30000000
last = list(numbers)[-1]
t_last = numbers[last]

while i < th:
    if t_last['tf'] is None:
        last = 0
    else:
        last = t_last['tl'] - t_last['tf']
    
    t_last = get_replace(numbers, last, i)
    i += 1

answer = last
print(answer)
