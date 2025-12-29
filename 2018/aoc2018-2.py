import os

with open(os.path.join('data', 'aoc2.txt')) as file:
    twice = trice = 0
    for line in map(str.strip, file):
        stop2 = stop3 = False
        for c in line:
            ct = line.count(c)
            if not stop2 and ct == 2:
                twice += 1
                stop2 = True
            if not stop3 and ct == 3:
                trice += 1
                stop3 = True
            if stop2 and stop3:
                break

    print(twice * trice)
