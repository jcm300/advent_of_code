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
valid_tickets = []
for ticket in nearby_tickets:
    for f in ticket:
        for rule in rules:
            if rule['l1'] <= f <= rule['m1'] or rule['l2'] <= f <= rule['m2']:
                break
        else:
            break
    else:
        valid_tickets.append(ticket)

def_fields = {}
unk_fields = {}
for ticket in valid_tickets:
    for i, f in enumerate(ticket):
        fields = []
        
        if i in def_fields.values():
            continue

        for rule in rules:
            if (rule['n'] not in def_fields and (
                rule['l1'] <= f <= rule['m1'] or
                rule['l2'] <= f <= rule['m2']
            )):
                fields.append(rule['n'])
        
        if len(fields) == 1:
            field = fields[0]
            def_fields[field] = i

            if unk_fields.get(i):
                del unk_fields[i]

            for k in unk_fields.keys():
                if field in unk_fields[k]:
                    unk_fields[k].remove(field)
        else:
            unk = unk_fields.get(i)

            if unk:
                inter = list(set(unk) & set(fields))

                if len(inter) == 1:
                    field = inter[0]
                    def_fields[field] = i
                    del unk_fields[i]

                    for k in unk_fields.keys():
                        if field in unk_fields[k]:
                            unk_fields[k].remove(field)
                else:
                    unk_fields[i] = inter
            else:
                unk_fields[i] = fields

while len(unk_fields):
    for k in unk_fields.keys():
        if len(unk_fields[k]) == 1:
            n = unk_fields[k][0]
            def_fields[n] = k
            del unk_fields[k]

            for unk in unk_fields.keys():
                if n in unk_fields[unk]:
                    unk_fields[unk].remove(n)

            break

answer = 1
for field, pos in def_fields.items():
    if re.match(r'departure', field):
        answer *= my_ticket[pos]

print(def_fields)
print(answer)
