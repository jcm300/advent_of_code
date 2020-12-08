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

for line in file_data.readlines():
    line = line.replace('.\n', '')
    parts = line.split(' bags contain')

    rule_key = parts[0]
    values = parts[1].split(',')
    rule = {}

    for value in values:
        value = value.replace(' bags', '')
        value = value.replace(' bag', '')[1:]

        if value != 'no other':
            match = re.search(r'^(\d+) ((\w| )+)$', value)
            if match:
                rule[match.group(2)] = int(match.group(1))

    rules[rule_key] = rule

# Get answer

def contain(bag, n, rules):
    if bag in rules and rules[bag] != {}:
        for need_bag, n_bags in rules[bag].items():
            n += n_bags + n_bags * contain(need_bag, 0, rules)

        return n
    else:
        return 0

answer = contain('shiny gold', 0, rules)
print(answer)
