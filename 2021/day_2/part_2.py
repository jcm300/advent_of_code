import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
commands = []
for line in file_data.readlines():
    commands.append(line.split(' '))

# Get answer
horizontal_pos = 0
depth_pos = 0
aim = 0

for command in commands:
    direction = command[0]
    value = int(command[1])

    if direction == 'forward':
        horizontal_pos += value
        depth_pos += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value

answer = horizontal_pos * depth_pos
print(answer)
