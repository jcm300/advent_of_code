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

def valid_year(year, min_y, max_y):
    is_valid = False

    if re.match(r'^\d{4}$', year):
        year = int(year)
        is_valid = year >= min_y and year <= max_y

    return is_valid

def valid_height(height):
    is_valid = False
    metric = height[-2:]

    try:
        value = int(height[:-2])
    except:
        return is_valid

    if metric == 'cm':
        is_valid = value >= 150 and value <= 193
    elif metric == 'in':
        is_valid = value >= 59 and value <= 76

    return is_valid

for passport in passports:
    if all(field in passport for field in required_fields):
        byr = valid_year(passport['byr'], 1920, 2002)
        iyr = valid_year(passport['iyr'], 2010, 2020)
        eyr = valid_year(passport['eyr'], 2020, 2030)
        hgt = valid_height(passport['hgt'])
        hcl = re.match(r'^#[0-9a-f]{6}$', passport['hcl'])
        ecl = re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', passport['ecl'])
        pid = re.match(r'^\d{9}$', passport['pid'])

        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid_passports += 1

print(valid_passports)
