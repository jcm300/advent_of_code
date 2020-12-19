import operator
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
expressions = []

def parse_exp(exp, i, l):
    ret = []

    while i < l and exp[i] != ')':
        if exp[i] == '(':
             e, i = parse_exp(exp, i+1, l)
             ret.append(e)
        elif re.match(r'^[0-9]+$', exp[i]):
            ret.append(int(exp[i]))
        else:
            op = operator.add if exp[i] == '+' else operator.mul
            ret.append(op)
        i += 1

    return ret, i

for line in file_data.readlines():
    line = line.replace('\n', '')

    opers = re.split(r'([()])| ([+*]) ', line)
    while '' in opers:
        opers.remove('')
    while None in opers:
        opers.remove(None)

    e, i = parse_exp(opers, 0, len(opers))
    expressions.append(e)

# Get answer

def calc_expr(expr):
    ret = 0

    for i, o in enumerate(expr):
        if isinstance(o, list):
            expr[i] = calc_expr(o)

    while operator.add in expr:
        for i, o in enumerate(expr):
            if o == operator.add:
                v1 = expr.pop(i-1)
                v2 = expr.pop(i)
                expr[i-1] = o(v1, v2)

    ret = expr.pop(0)
    l = len(expr)
    i = 0
    while i < l and i+1 < l:
        o = expr.pop(0)
        v = expr.pop(0)
        ret = o(ret, v)
        i += 2

    return ret

answer = 0
for expr in expressions:
    answer += calc_expr(expr)
print(answer)
