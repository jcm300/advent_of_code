import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
groups = []
group = []

for line in file_data.readlines():
    line = line.replace('\n', '')
    if line == '':
        groups.append(list(group))
        group = []
    else:
        group += [c for c in line if c not in group]

if len(group):
    groups.append(group)

# Get answer
sum_counts = sum(map(len, groups))
print(sum_counts)
