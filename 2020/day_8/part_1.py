import operator
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
ops = []

def str_to_op(st):
    if st == '+':
        return operator.add
    elif st == '-':
        return operator.sub
    else:
        return operator.add

for line in file_data.readlines():
    line = line.replace('.\n', '')
    parts = line.split(' ')

    op = {
        'name': parts[0],
        'signal': str_to_op(parts[1][0]),
        'value': int(parts[1][1:]),
        'executed': False,
    }
    ops.append(op)

# Get answer
pointer = 0
accumulator = 0
l = len(ops)

op = ops[pointer]
while not op['executed']:
    ops[pointer]['executed'] = True

    if op['name'] == 'acc':
        accumulator = op['signal'](accumulator, op['value'])
        pointer += 1
    elif op['name'] == 'jmp':
        pointer = op['signal'](pointer, op['value'])
    else: # op['name'] == 'nop'
        pointer += 1

    if pointer < l:
        op = ops[pointer]
    else:
        break

print(accumulator)
