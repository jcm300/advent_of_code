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
my_seat = None
seat_ids_sorted = sorted(seat_ids)

for i, seat_id in enumerate(seat_ids_sorted):
    if seat_id + 1 != seat_ids_sorted[i + 1]:
        my_seat = seat_id + 1
        break

print(my_seat)
