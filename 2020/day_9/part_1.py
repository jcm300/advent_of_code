import os
import re
import sys

# Read arguments
if len(sys.argv) != 3:
    raise ValueError('Please provide a filename input and length preamble')

filename = sys.argv[1]
preamble_len = int(sys.argv[2])

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
numbers = []

for line in file_data.readlines():
    line = line.replace('.\n', '')
    
    numbers.append(int(line))

# Get answer

def found_sum(number, preamble):
    for i, numb_1 in enumerate(preamble):
        for numb_2 in preamble[i:]:
            if numb_1 + numb_2 == number:
                return True

    return False

preamble = []
number = None
length_n = len(numbers)
i = 0

while i < preamble_len and i < length_n:
    preamble.append(numbers[i])
    i += 1

while i < length_n and number is None:
    if not found_sum(numbers[i], preamble):
        number = numbers[i]
    else:
        preamble.pop(0)
        preamble.append(numbers[i])
        i += 1

print(number)
