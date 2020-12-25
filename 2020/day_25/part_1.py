import os
import re
import sys
from collections import Counter

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
public_keys = []
for line in file_data.readlines():
    line = line.replace('\n', '')
    public_keys.append(int(line))

# Get answer

def trans_subj(subj_n, loop_size):
    i = 0
    ret = 1

    while i < loop_size:
        ret *= subj_n
        ret = ret % 20201227
        i += 1

    return ret

def find_loop_size(subj_n, pub_key):
    i = 0
    ret = 1

    while ret != pub_key:
        ret *= subj_n
        ret = ret % 20201227
        i += 1

    return i

card_loop_size = find_loop_size(7, public_keys[0])
door_loop_size = find_loop_size(7, public_keys[1])
encryption_key_1 = trans_subj(public_keys[1], card_loop_size)
encryption_key_2 = trans_subj(public_keys[0], door_loop_size)
print(encryption_key_1)
print(encryption_key_2)
