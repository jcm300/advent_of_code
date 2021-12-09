import os
import re
import sys
import multiprocessing
from functools import reduce

def check_lantern_fishes(lantern_fishes):
    days = 256

    for day in range(days):
        for i in range(len(lantern_fishes)):
            if lantern_fishes[i] == 0:
                lantern_fishes[i] = 6
                lantern_fishes.append(8)

            else:
                lantern_fishes[i] -= 1

    return len(lantern_fishes)

if __name__ == "__main__":

    # Read arguments
    if len(sys.argv) != 2:
        raise ValueError('Please provide a filename input')

    filename = sys.argv[1]

    # Read file
    file_data = open(os.getcwd() + '/' + filename, 'r')

    #
    # Parse file
    #
    text = file_data.read().replace('\n', '')
    lantern_fishes = list(map(int, text.split(',')))

    #
    # Get answer
    #
    no_threads = multiprocessing.cpu_count()
    no_fishes = len(lantern_fishes)

    if no_threads > no_fishes:
        no_threads = no_fishes

    d = int(no_fishes / no_threads)
    sub_arrays = [lantern_fishes[i:i+d] for i in range(0, no_fishes, d)]

    if len(sub_arrays) > no_threads:
        sub_arrays[-2] = sub_arrays[-2] + sub_arrays[-1]
        del sub_arrays[-1]

    pool = multiprocessing.Pool(no_threads)
    sub_arrays_res = pool.map(check_lantern_fishes, sub_arrays)
    pool.close()

    answer = sum(sub_arrays_res)
    print(answer)
