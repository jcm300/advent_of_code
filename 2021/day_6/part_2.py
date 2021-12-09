import os
import re
import sys
import multiprocessing
from functools import reduce

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
days = 256
grouped_fishes = {}

for i in range(9):
    count = lantern_fishes.count(i)
    grouped_fishes[i] = count

for day in range(days): 
    zeros = grouped_fishes[0]

    for i in grouped_fishes:
        if i < 8:
            grouped_fishes[i] = grouped_fishes[i+1]

    grouped_fishes[6] += zeros
    grouped_fishes[8] = zeros

answer = 0

for fishes in grouped_fishes:
    answer += grouped_fishes[fishes]

print(answer)
