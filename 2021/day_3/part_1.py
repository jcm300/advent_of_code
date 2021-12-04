import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
lines = [line.replace('\n', '') for line in file_data.readlines()]
binary_values = [''] * (len(lines[0]) if len(lines) > 0 else 0)

for line in lines:
    for i, binary in enumerate(line):
        binary_values[i] += binary

# Get answer
gama_rate_bin = ''
epsilon_rate_bin = ''

for binary_value in binary_values:
    zeros = binary_value.count('0')
    ones = binary_value.count('1')

    if zeros > ones:
        gama_rate_bin += '0'
        epsilon_rate_bin += '1'
    else:
        gama_rate_bin += '1'
        epsilon_rate_bin += '0'

answer = int(gama_rate_bin, 2) * int(epsilon_rate_bin, 2)
print(answer)
