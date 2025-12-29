import os
from collections import defaultdict


def get_numval(val):
    if isinstance(val, int):
        return val
    else:
        return data[val]


def try_number(x):
    try:
        return int(x)
    except ValueError:
        return x


prog = []
with open(os.path.join('data', 'aoc18.txt')) as f:
    for line in f:
        inst, *info = line.rstrip().split()
        prog.append([inst] + [try_number(x) for x in info])

print(prog)

data = defaultdict(lambda: 0)

i = 0
last = 0
length = len(prog)

while 0 <= i < length:
    inst, *info = prog[i]
    if inst == 'snd':
        last = get_numval(*info)
    elif inst == 'rcv':
        val = get_numval(*info)
        if val:
            print(last)
            break
    else:
        what, val = info
        if inst == 'set':
            data[what] = get_numval(val)
        elif inst == 'add':
            data[what] += get_numval(val)
        elif inst == 'mul':
            data[what] *= get_numval(val)
        elif inst == 'mod':
            data[what] = data[what] % get_numval(val)
        elif inst == 'jgz':
            my_what = get_numval(what)
            if my_what > 0:
                i += get_numval(val)
                continue
    i += 1
