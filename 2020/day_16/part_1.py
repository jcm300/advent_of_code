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
rules = []
my_ticket = []
nearby_tickets = []

flag = 0 # 0 for rules, 1 for my ticket, 2 for nearby tickets
for line in file_data.readlines():
    line = line.replace('\n', '')

    if line == '':
        continue
    elif line in ['your ticket:', 'nearby tickets:']:
        flag += 1
        continue

    if flag == 0:
        m = re.search(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$', line)
        rules.append({
            'n': m.group(1),
            'l1': int(m.group(2)),
            'm1': int(m.group(3)),
            'l2': int(m.group(4)),
            'm2': int(m.group(5)),
        })
    else:
        fs = list(map(int, line.split(',')))

        if flag == 1:
            my_ticket = fs
        else:
            nearby_tickets.append(fs)

# Get answer
answer = 0
for ticket in nearby_tickets:
    for f in ticket:
        for rule in rules:
            if rule['l1'] <= f <= rule['m1'] or rule['l2'] <= f <= rule['m2']:
                break
        else:
            answer += f
            break

print(answer)
