import os

with open(os.path.join('data', 'aoc9.txt')) as file:
    line = file.read().strip()

disk = []

blank = False
i = 0
for c in map(int, line):
    if blank:
        for _ in range(int(c)):
            disk.append(None)
    else:
        for _ in range(int(c)):
            disk.append(i)
        i += 1
    blank = not blank

for pos, val in enumerate(disk):
    if val is None:
        new = None
        while new is None:
            new = disk.pop()
        disk[pos] = new

result = sum(pos * val for pos, val in enumerate(disk))

print(result)
