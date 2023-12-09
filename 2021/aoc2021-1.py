import os

last = -1
total = -1
values = []
with open(os.path.join('data', 'aoc1.txt'), 'r') as file:
    for line in file:
        n = int(line)
        values.append(n)
        if n > last:
            total += 1
        last = n

print(total)

last = -1
total = -1
for win in zip(values[2:], values[1:], values):
    n = sum(win)
    if n > last:
        total += 1
    last = n

print(total)
