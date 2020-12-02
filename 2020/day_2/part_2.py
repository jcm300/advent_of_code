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
parsed_lines = []

for line in file_data.readlines():
    parts = line.split(': ')
    policies = re.search(r'^(\d+)-(\d+) ([a-z])$', parts[0]) 

    parsed_line = {
        'pos_1': int(policies.group(1)) - 1,
        'pos_2': int(policies.group(2)) - 1,
        'pattern': policies.group(3), 
        'password': parts[1].replace('\n', ''),
    }
    parsed_lines.append(parsed_line)

# Get answer
valid_passwords = 0
for parsed_line in parsed_lines:
    pos_1_eq = parsed_line['password'][parsed_line['pos_1']] == parsed_line['pattern']
    pos_2_eq = parsed_line['password'][parsed_line['pos_2']] == parsed_line['pattern']

    if pos_1_eq ^ pos_2_eq:
        valid_passwords += 1

print(valid_passwords)
