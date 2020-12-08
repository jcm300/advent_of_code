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

def contain(bag, n, bags, rules):
    for key, rule in rules.items():
        if bag in rule and key not in bags and n <= rule[bag]:
            bags.append(key)
            bags = contain(key, 1, bags, rules)

    return bags

bags = contain('shiny gold', 1, [], rules)
answer = len(bags)
print(answer)
