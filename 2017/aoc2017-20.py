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

best = None
while True:
    for pid in pos:
        pos[pid] = incr(pos[pid], vel[pid])
        vel[pid] = incr(vel[pid], acc[pid])
    dist = {pid: abs(x) + abs(y) + abs(z) for pid, (x, y, z) in pos.items()}
    new_best = min(dist, key=dist.get)
    if new_best != best:
        best = new_best
        print(best)
