import os
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
    number = int(line)
    numbers.append(number)

# Get answer
n = len(numbers)
found_numbers = 0, 0
for i, number_1 in enumerate(numbers):
    for number_2 in numbers[i+1:]:
        if number_1 + number_2 == 2020:
            found_numbers = number_1, number_2
            break

    if found_numbers[0] != 0 and found_numbers[1] != 0:
        break

answer = found_numbers[0] * found_numbers[1]
print(answer)
