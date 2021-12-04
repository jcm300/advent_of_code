import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
matrix = [line.replace('\n', '') for line in file_data.readlines()]

# Get answer

def get_lines(h_pos, matrix, signal):
    v_line = ''

    for h_line in matrix:
        v_line += h_line[h_pos]

    zeros = v_line.count('0')
    ones = v_line.count('1')

    if ones >= zeros:
        bit_criteria = '1' if signal else '0'
    else:
        bit_criteria = '0' if signal else '1'

    ret_lines = [
        h_line for h_line in matrix
        if h_line[h_pos] == bit_criteria
    ]
    return ret_lines

def get_number(matrix, signal):
    h_pos = 0

    numbers = get_lines(h_pos=h_pos, matrix=matrix, signal=signal)

    while len(numbers) > 1:
        h_pos += 1
        numbers = get_lines(h_pos=h_pos, matrix=numbers, signal=signal)

    return numbers[0]

oxygen_rate = get_number(matrix=matrix, signal=True)
co2_rate = get_number(matrix=matrix, signal=False)

answer = int(oxygen_rate, 2) * int(co2_rate, 2)
print(answer)
