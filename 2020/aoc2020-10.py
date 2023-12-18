import os

jolts = []

with open(os.path.join('data', 'aoc10.txt')) as f:
    for line in f:
        num = int(line.rstrip())
        jolts.append(num)

jolts.append(max(jolts) + 3)
jolts.append(0)
jolts.sort()

one_diff = three_diff = 0
prev = 0

for num in jolts:
    diff = num - prev
    if diff == 1:
        one_diff += 1
    elif diff == 3:
        three_diff += 1
    prev = num

print(one_diff * three_diff)

paths = dict.fromkeys(jolts, 0)
paths[0] = 1
for node in jolts:
    this = paths[node]
    for i in (1, 2, 3):
        adj = node+i
        if adj in paths:
            paths[adj] += this

print(paths[jolts[-1]])
