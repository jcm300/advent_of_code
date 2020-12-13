import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
lines = file_data.readlines()
buses_aux = lines[1].split(',')
buses = []

t = 0
for bus in buses_aux:
    if bus != 'x':
        buses.append({'bus': int(bus), 'd': t})
    t += 1

# Get answer
answer = 0

jump = buses[0]['bus']
for bus in buses[1:]:
    while (answer + bus['d']) % bus['bus'] != 0:
        answer += jump

    jump *= bus['bus']

print(answer)
