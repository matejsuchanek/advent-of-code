import os
from collections import defaultdict


def get_numval(val):
    if val in regs:
        return data[val]
    else:
        return int(val)


def run(i=0):
    res = 0
    while 0 <= i < length:
        print(i, *lines[i])
        inst, what, val = lines[i]
        if inst == 'set':
            data[what] = get_numval(val)
        elif inst == 'sub':
            data[what] -= get_numval(val)
        elif inst == 'mul':
            res += 1
            data[what] *= get_numval(val)
        elif inst == 'jnz':
            my_what = get_numval(what)
            if my_what:
                i += get_numval(val)
                continue
        i += 1
    return res


lines = []
with open(os.path.join('data', 'aoc23.txt')) as file:
    for line in file:
        lines.append(line.split())

length = len(lines)
regs = set('abcdefgh')
data = defaultdict(lambda: 0)
print(run())
