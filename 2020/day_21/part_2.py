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

i_a = {}
while len(ingr_aller):
    for a, ins in ingr_aller.items():
        if len(ins) == 1:
            i = ins[0]
            i_a[i] = a 

            for ang, ings in ingr_aller.items():
                if i in ings:
                    ingr_aller[ang].remove(i)

            ingr_aller.pop(a)
            break

sorted_tuples = sorted(i_a.items(), key=lambda e: e[1])
sorted_dict = {k: v for k, v in sorted_tuples}
answer = ','.join(sorted_dict.keys())
print(answer)
