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
lines = []

for line in file_data.readlines():
    l = line.replace('\n', '')
    lines.append(l)

#
# Get answer
#
MAP_CLOSE_SYMBOL = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

MAP_CLOSE_SYMBOL_POINTS = {
    None: 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def check_line(line):
    stack = []
    error_symbol = None

    for s in line:
        if s in ['(', '[', '{', '<']:
            stack.append(s)
        elif s in [')', ']', '}', '>']:
            if MAP_CLOSE_SYMBOL[s] == stack[-1]:
                stack.pop()
            else:
                error_symbol = s
                break
        else:
            error_symbol = s
            break

    if stack:
        #TODO: for now ignore
        pass

    return error_symbol

answer = 0
for line in lines:
    error_symbol = check_line(line)
    answer += MAP_CLOSE_SYMBOL_POINTS[error_symbol]

print(answer)
