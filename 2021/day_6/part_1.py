import os
import re
import sys

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
lantern_fishes = list(map(int, text.split(',')))

#
# Get answer
#
days = 80

for day in range(days):
    for i in range(len(lantern_fishes)):
        if lantern_fishes[i] == 0:
            lantern_fishes[i] = 6
            lantern_fishes.append(8)

        else:
            lantern_fishes[i] -= 1

answer = len(lantern_fishes)
print(answer)
