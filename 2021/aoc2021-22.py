import os

enabled = set()
make_range = lambda a, b: range(max(a, -50), min(b, 50) + 1)

with open(os.path.join('data', 'aoc22.txt'), 'r') as file:
    for line in file:
        left, right = line.split()
        on = left == 'on'

        dims = []
        for s in right.split(','):
            l, u = map(int, s[2:].split('..'))
            dims.append((l, u))

        for x in make_range(*dims[0]):
            for y in make_range(*dims[1]):
                for z in make_range(*dims[2]):
                    t = (x, y, z)
                    if on:
                        enabled.add(t)
                    elif t in enabled:
                        enabled.remove(t)

    print(len(enabled))
