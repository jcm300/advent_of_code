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
rules = {}
messages = []

flag = 0 # 0 -> rules, 1 -> messages
for line in file_data.readlines():
    line = line.replace('\n', '')

    if line == '':
        flag = 1
        continue
    
    if flag == 0:
        parts = line.split(': ')
        m = re.match(r'^"(\w+)"$', parts[1])
        
        if m:
            sub_parts = m.group(1)
        else:
            sub_parts = parts[1].split()
        
        rules[parts[0]] = sub_parts
    else:
        messages.append(line)

def def_rules(rule, rules):
    ret = ''
    loop = -1

    r = rules[rule]
    if isinstance(r, list):
        if rule in r:
            while r[0] != '|':
                r.pop(0)
            r.pop(0)

        for e in r:
            if e == rule:
                loop = len(ret)
                if rule == '8':
                    flag = 2
                else:
                    flag = 3
            elif e == '|' or not re.match(r'^[0-9]+$', e):
                ret += e
            else:
                rules = def_rules(e, rules)
                ret += rules[e]

        if '|' in r:
            ret = '(' + ret +')'

        if loop >= 0 and flag == 2:
            ret += '+'
        elif loop >= 0 and flag == 3:
            part_1 = ret[:loop]
            part_2 = ret[loop:]
            # Not the best code :|
            ret = '(' + part_1 + part_2 + '|' + \
                  part_1 * 2 + part_2 * 2 + '|' + \
                  part_1 * 3 + part_2 * 3 + '|' + \
                  part_1 * 4 + part_2 * 4 + '|' + \
                  part_1 * 5 + part_2 * 5 + ')'

        rules[rule] = ret

    return rules

rules = def_rules('0', rules)

# Get answer
answer = 0
for msg in messages:
    if re.match(r'^' + rules['0'] + r'$', msg):
        answer += 1
print(answer)
