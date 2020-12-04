import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
passports = []
passport = {}

for line in file_data.readlines():
    line = line.replace('\n', '')
    if line == '':
        passports.append(passport)
        passport = {}
    else:
        fields = line.split(' ')

        for field in fields:
            key_value = field.split(':')
            passport[key_value[0]] = key_value[1]

if passport != {}:
    passports.append(passport)

# Get answer
valid_passports = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl','ecl', 'pid']
optional_fields = ['cid']

for passport in passports:
    if all(field in passport for field in required_fields):
        valid_passports += 1

print(valid_passports)
