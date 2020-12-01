import operator
import os
import sys
from functools import reduce
from itertools import product

# Read arguments
if len(sys.argv) != 3:
    raise ValueError('Please provide a filename input and the entries number')

filename = sys.argv[1]
entries = int(sys.argv[2])

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
numbers = []

for line in file_data.readlines():
    number = int(line)
    numbers.append(number)

# Get answer
n = len(numbers)
found_numbers = []
boundaries_list = []
i = 0

while i < entries:
    boundaries_list.append([i,n,1])
    i += 1

for indexes in product(*(range(*b) for b in boundaries_list)):
    aux_numbers = []
    for index in indexes:
        aux_numbers.append(numbers[index])

    if sum(aux_numbers) == 2020:
        found_numbers = aux_numbers
        break

answer = reduce(operator.mul, found_numbers)
print(answer)
