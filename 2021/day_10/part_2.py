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

MAP_OPEN_SYMBOL = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

MAP_CLOSE_SYMBOL_POINTS = {
    None: 0,
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
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

    if error_symbol:
        return None
    else:
        return stack

def autocomplete(stack):
    s_complete = ''

    for s in reversed(stack):
        s_complete += MAP_OPEN_SYMBOL[s]

    return s_complete

def completion_score(s_complete):
    score = 0

    for s in s_complete:
        score *= 5
        score += MAP_CLOSE_SYMBOL_POINTS[s]

    return score

scores = []
for line in lines:
    stack = check_line(line)

    if stack:
        s_complete = autocomplete(stack)
        scores.append(completion_score(s_complete))

sorted_scores = sorted(scores)
answer = sorted_scores[math.floor(len(sorted_scores)/2)]
print(answer)
