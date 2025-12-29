import os
from collections import defaultdict, deque


def get_numval(data, val):
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


def run(data, i, in_queue, out_queue):
    length = len(prog)

    while 0 <= i < length:
        inst, *info = prog[i]
        if inst == 'snd':
            out_queue.append(get_numval(data, *info))
        elif inst == 'rcv':
            if not in_queue:
                return i
            data[info[0]] = in_queue.popleft()
        else:
            what, val = info
            if inst == 'set':
                data[what] = get_numval(data, val)
            elif inst == 'add':
                data[what] += get_numval(data, val)
            elif inst == 'mul':
                data[what] *= get_numval(data, val)
            elif inst == 'mod':
                data[what] = data[what] % get_numval(data, val)
            elif inst == 'jgz':
                my_what = get_numval(data, what)
                if my_what > 0:
                    i += get_numval(data, val)
                    continue
        i += 1

    return None


regs = [defaultdict(lambda: 0), defaultdict(lambda: 0)]
for x in [0, 1]:
    regs[x]['p'] = x

result = 0
pid = 0
in_queues = [deque(), deque()]
instr = [0, 0]
alive = [True, True]
waiting = [False, False]
while alive[pid] and not all(waiting):
    outq = in_queues[1-pid]
    before = len(outq)
    out = run(regs[pid], instr[pid], in_queues[pid], outq)
    diff = len(outq) - before
    if diff:
        waiting[1-pid] = False
    if pid == 1:
        result += diff
    if out is None:
        alive[pid] = False
    else:
        instr[pid] = out
        waiting[pid] = True
    pid = 1 - pid

print(result)
