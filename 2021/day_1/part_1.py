import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
increased_times = 0
previous_depth = None

for line in file_data.readlines():
    depth = int(line)

    if previous_depth and depth > previous_depth:
        increased_times += 1

    # Update previous depth
    previous_depth = depth

# Get answer
print(increased_times)
