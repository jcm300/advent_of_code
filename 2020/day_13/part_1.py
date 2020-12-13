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
lines = file_data.readlines()
depart = int(lines[0])

buses_aux = lines[1].split(',')
buses = []

for bus in buses_aux:
    if bus != 'x':
        buses.append(int(bus))

# Get answer
bus_to_use = None
time_bus = sys.maxsize

for bus in buses:
    r = depart % bus
    p_bus = depart - r + bus

    if p_bus < time_bus:
        bus_to_use = bus
        time_bus = p_bus

answer = (time_bus - depart) * bus_to_use
print(answer)
