import os


def update():
    for depth, (pos, dr) in scanners.items():
        pos += dr
        if pos == 1 or pos == layers[depth]:
            dr = -dr
        scanners[depth] = (pos, dr)


def run(quick=False):
    hits = total = 0
    for pico in range(max(layers)+1):
        if pico in scanners and scanners[pico][0] == 1:
            hits += 1
            if quick:
                return hits, total
            total += pico * layers[pico]
        update()
    return hits, total


layers = {}
scanners = {}

with open(os.path.join('data', 'aoc13.txt')) as file:
    for line in map(str.rstrip, file):
        depth, rng = map(int, line.split(': '))
        layers[depth] = rng

scanners = dict.fromkeys(layers, (1, 1))
last_init = dict(scanners)
hits, total = run()
print(total)

delay = 0
while hits:
    delay += 1
    scanners.update(last_init)
    update()
    last_init.update(scanners)
    hits, _ = run(True)

print(delay)
