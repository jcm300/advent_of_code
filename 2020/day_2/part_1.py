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
        'min': int(policies.group(1)),
        'max': int(policies.group(2)),
        'pattern': policies.group(3), 
        'password': parts[1].replace('\n', ''),
    }
    parsed_lines.append(parsed_line)

# Get answer
valid_passwords = 0
for parsed_line in parsed_lines:
    matches = len(re.findall(parsed_line['pattern'], parsed_line['password']))

    if matches >= parsed_line['min'] and matches <= parsed_line['max']:
        valid_passwords += 1
print(valid_passwords)
