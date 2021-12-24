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
entries = []

for line in file_data.readlines():
    l = line.replace('\n', '')
    patterns, outputs = l.split(' | ')

    entries.append({
        'patterns': patterns.split(' '),
        'outputs': outputs.split(' '),
    })

#
# Get answer
#
answer = 0

for entry in entries:
    for output in entry['outputs']:
        if len(output) in [2, 3, 4, 7]:
            answer += 1

print(answer)
