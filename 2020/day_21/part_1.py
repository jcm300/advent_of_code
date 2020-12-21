import os
import re
import sys
from functools import reduce

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
foods = []
for line in file_data.readlines():
    line = line.replace('\n', '')
    
    m = re.match(r'^(.*?) \(contains (.*?)\)$', line) 
    ingredients = m.group(1).split()
    allergens = m.group(2).split(', ')
    foods.append({'i': ingredients, 'a': allergens})

# Get answer
ingr_aller = {}

for food in foods:
    for a in food['a']:
        if a in ingr_aller:
            ingr_aller[a] = list(set(ingr_aller[a]) & set(food['i']))
        else:
            ingr_aller[a] = food['i']

ingrs = list(set(reduce(lambda a, b: a+b, ingr_aller.values())))
answer = 0
for food in foods:
    for i in food['i']:
        if i not in ingrs:
            answer += 1
print(answer)
