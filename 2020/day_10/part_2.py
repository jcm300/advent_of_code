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
numbers = []

for line in file_data.readlines():
    line = line.replace('.\n', '')
    
    numbers.append(int(line))

# Get answer
numbers.append(0)
numbers.append(max(numbers) + 3)
numbers = sorted(numbers)

difs = []
i = 0
n = len(numbers)

# Calc difs between numbers
while i < n and i + 1 < n:
    difs.append(numbers[i + 1] - numbers[i])
    i += 1

i = 0
n = len(difs)
seq_1s = []

# Calc number of sequecial 1's
while i < n:
    j = 0
    while difs[i] == 1 and i < n:
        j += 1
        i += 1

    seq_1s.append(j)
    i += 1

# Remove 0s
while 0 in seq_1s:
    seq_1s.remove(0)

answer = 1
# Calc answer with numbers of sequencial 1's
for n_seq in seq_1s:
    if n_seq > 3:
        r = n_seq % 3
    else:
        r = 0

    answer *= pow(2, n_seq - 1) - r

print(answer)
