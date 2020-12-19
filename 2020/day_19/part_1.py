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

    r = rules[rule]
    if isinstance(r, list):
        for e in r:
            if e == '|' or not re.match(r'^[0-9]+$', e):
                ret += e
            else:
                rules = def_rules(e, rules)
                ret += rules[e]

        if '|' in r:
            ret = '(' + ret +')'

        rules[rule] = ret

    return rules

rules = def_rules('0', rules)

# Get answer
answer = 0
for msg in messages:
    if re.match(r'^' + rules['0'] + r'$', msg):
        answer += 1
print(answer)
