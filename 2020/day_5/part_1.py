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
seat_ids = []

for line in file_data.readlines():
    line = line.replace('\n', '')

    # Convert to binary
    line = re.sub(r'B|R', '1', line)
    line = re.sub(r'F|L', '0', line)

    # Convert binary to decimal
    row = int(line[:7], 2)
    col = int(line[7:], 2)

    seat_id = row * 8 + col
    seat_ids.append(seat_id)

# Get answer
high_seat_id = max(seat_ids)
print(high_seat_id)
