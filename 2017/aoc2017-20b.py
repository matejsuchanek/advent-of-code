import os


def incr(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])


pos = {}
vel = {}
acc = {}

with open(os.path.join('data', 'aoc20.txt')) as file:
    for pid, line in enumerate(map(str.rstrip, file)):
        parts = line.split(', ')
        parts = [part[3:-1] for part in parts]
        pos[pid] = tuple(map(int, parts[0].split(',')))
        vel[pid] = tuple(map(int, parts[1].split(',')))
        acc[pid] = tuple(map(int, parts[2].split(',')))

for _ in range(10_000):  # GUESS
    inverse = {}
    remove = set()

    for pid in pos:
        vel[pid] = incr(vel[pid], acc[pid])
        pos[pid] = incr(pos[pid], vel[pid])

        conflict = inverse.get(pos[pid])
        if conflict is not None:
            remove.add(conflict)
            remove.add(pid)
        else:
            inverse[pos[pid]] = pid

    for pid in remove:
        del pos[pid]
        del vel[pid]
        del acc[pid]

print(len(pos))
