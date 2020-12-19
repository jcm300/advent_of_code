import os
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
state = []

for line in file_data.readlines():
    line = line.replace('\n', '')
    state.append(list(map(lambda x: 1 if x == '#' else 0, line)))

# Get answer

def actives_around(x, y, z, w, cubes):
    actives = 0
    lw = len(cubes)
    lz = len(cubes[0])
    ly = len(cubes[0][0])
    lx = len(cubes[0][0][0])

    for e in [w-1, w, w+1]:
        for f in [z-1, z, z+1]:
            for j in [y-1, y, y+1]:
                for i in [x-1, x, x+1]:
                    if 0 <= i < lx and 0 <= j < ly and 0 <= f < lz and 0 <= e < lw:
                        actives += cubes[e][f][j][i]

    return actives

def cal_state(cubes):
    cubes_ret = []
    
    for w, w_plane in enumerate(cubes):
        w_plane_ret = []
        for z, z_plane in enumerate(w_plane):
            z_plane_ret = []
            for y, y_plane in enumerate(z_plane):
                y_plane_ret = []
                for x, v in enumerate(y_plane):
                    act = actives_around(x, y, z, w, cubes) - v

                    if (v == 1 and act in [2, 3]) or (v == 0 and act == 3):
                        c = 1
                    else:
                        c = 0

                    y_plane_ret.append(c)
                z_plane_ret.append(y_plane_ret)
            w_plane_ret.append(z_plane_ret)
        cubes_ret.append(w_plane_ret)

    return cubes_ret

def zero_line(l):
    return [0 for j in range(l)]

def zeros(l):
    ret = []
    for i in range(l):
        ret.append(zero_line(l))
    return ret

def czeros(l):
    c = []
    for i in range(l):
        c.append(zeros(l))
    return c

cicle = 0
cicles = 6
li = len(state)
cubes = []
s_final = []
s_cube = []

for w in range(cicles):
    s_final.append(zero_line(li+2*cicles))

for w in range(li):
    state[w] = zero_line(cicles) + state[w] + zero_line(cicles)

s_final = s_final + state + s_final

for w in range(2*cicles):
    s_cube.append(zeros(li+2*cicles))

s_cube = s_cube + [s_final] + s_cube

for w in range(2*cicles):
    cubes.append(czeros(li+2*cicles))

cubes = cubes + [s_cube] + cubes

while cicle < cicles:
    cubes = cal_state(cubes)
    cicle += 1

answer = 0
for w in cubes:
    for z in w:
        for y in z:
            answer += sum(y)

print(answer)
