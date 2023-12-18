import os

with open(os.path.join('data', 'aoc13.txt')) as f:
    time = int(next(f).rstrip())
    buses = [(i, int(x)) for i, x in enumerate(next(f).split(',')) if x != 'x']

mods = {bus: time % bus for _, bus in buses}
departs = {bus: time + (bus - m) for bus, m in mods.items()}

print(min(departs, key=lambda k: departs[k]) * (min(departs.values()) - time))

t, coef = buses[0]
for incr, bus in buses[1:]:
    while ((t + incr) % bus) != 0:
        t += coef
    coef *= bus

print(t)
