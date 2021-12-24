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
        'patterns': sorted(patterns.split(' '), key=len),       
        'outputs': outputs.split(' '),
    })

#
# Get answer
#
answer = 0

for entry in entries:
    value = ''
    #  --- u ---
    #  |       |
    #  ul     ur
    #  |       |
    #  --- m ---
    #  |       |
    #  dl     dr
    #  |       |
    #  --- d ---
    
    # Find upper line
    u = ''
    for letter in entry['patterns'][1]:
        if letter not in entry['patterns'][0]:
            u = letter
            break

    # ur and dr can be any line of 1
    ur_dr = list(entry['patterns'][0])

    # ul and m can be any line of 4 that is not on 1
    ul_m = []
    for letter in entry['patterns'][2]:
        if letter not in entry['patterns'][0]:
            ul_m.append(letter)

    # dl and d can be any line of 8 that is not on 4 and that is not up line
    dl_d = []
    for letter in entry['patterns'][-1]:
        if letter not in entry['patterns'][2] and letter != u:
            dl_d.append(letter)

    # Find number
    for output in entry['outputs']:
        size = len(output)

        if size == 2:
            value += '1'
        elif size == 3:
            value += '7'
        elif size == 4:
            value += '4'
        elif size == 7:
            value += '8'
        elif size == 5:
            if ur_dr[0] in output and ur_dr[1] in output:
                value += '3'
            elif dl_d[0] in output and dl_d[1] in output:
                value += '2'
            else:
                value += '5'
        elif size == 6:
            if ur_dr[0] in output and ur_dr[1] in output:
                if dl_d[0] in output and dl_d[1] in output:
                    value += '0'
                else:
                    value += '9'
            else:
                value += '6'

    # Add value to answer
    answer += int(value)

print(answer)
