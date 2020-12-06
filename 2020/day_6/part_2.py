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

def intersection(group):
    ret = set()

    if len(group):
        ret = group[0]
        for p in group:
            ret = ret & p

    return ret

for line in file_data.readlines():
    line = line.replace('\n', '')
    if line == '':
        groups.append(intersection(group))
        group = []
    else:
        group.append(set(line))

if len(group):
    groups.append(intersection(group))

# Get answer
sum_counts = sum(map(len, groups))
print(sum_counts)
