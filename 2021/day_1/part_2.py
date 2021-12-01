import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
depths = []

for line in file_data.readlines():
    depths.append(int(line))

# Get answer
answer = 0
previous_sum = None
depth_size = len(depths)

for i in range(depth_size):
    if i+1 < depth_size and i+2 < depth_size:
        actual_sum = depths[i] + depths[i+1] + depths[i+2]

        if previous_sum and actual_sum > previous_sum:
            answer += 1

        previous_sum = actual_sum

print(answer)
