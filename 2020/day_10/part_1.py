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
numbers = []

for line in file_data.readlines():
    line = line.replace('.\n', '')
    
    numbers.append(int(line))

# Get answer
numbers.append(0)
numbers.append(max(numbers) + 3)
numbers = sorted(numbers)

difs = []
i = 0
n = len(numbers)

while i < n and i + 1 < n:
    difs.append(numbers[i + 1] - numbers[i])
    i += 1

n_1s = len(list(filter(lambda x: x == 1, difs)))
n_3s = len(list(filter(lambda x: x == 3, difs)))
answer = n_1s * n_3s

print(answer)
