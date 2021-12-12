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
    return sum([abs(pos - p) for pos in positions])

# Calculate median
sorted_positions = sorted(positions)
size = len(positions)
halp_pos = math.floor(size / 2) - 1

if size % 2 == 1:
    p = sorted_positions[halp_pos] 
    answer = fuel(p, positions)
else:
    p1 = sorted_positions[halp_pos]
    p2 = sorted_positions[halp_pos+1]
    p = p1

    min_fuel = None
    min_p = None
    while p <= p2:
        f = fuel(p, positions)

        if min_fuel is None or min_fuel > f:
            min_fuel = f
            min_p = p

        p += 1

    answer = min_fuel

print(answer)
