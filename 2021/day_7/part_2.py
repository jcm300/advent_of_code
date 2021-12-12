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
text = file_data.read().replace('\n', '')
positions = list(map(int, text.split(',')))

#
# Get answer
#
def fuel(p, positions):
    return sum([i for pos in positions for i in range(abs(pos - p) + 1)])

# Calculate mean
mean = sum(positions) / len(positions) 
pos = math.floor(mean)

f1 = fuel(pos, positions)
f2 = fuel(pos + 1, positions)

answer = f1 if f1 < f2 else f2
print(answer)
