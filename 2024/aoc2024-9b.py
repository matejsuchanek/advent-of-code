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

cur = len(disk) - 1
while disk[cur] is None:
    cur -= 1
i = disk[cur]
while i > 0:
    while disk[cur] != i:
        cur -= 1

    length = 0
    while disk[cur] == i:
        length += 1
        cur -= 1

    start = 0
    streak = 0
    for pos, val in enumerate(disk):
        if pos > cur:
            break
        if val is not None:
            start = pos + 1
            streak = 0
            continue
        streak += 1
        if streak == length:
            break

    if streak == length:
        for offset in range(length):
            disk[start+offset] = i
            disk[cur+1+offset] = None

    i -= 1

result = sum(pos * val for pos, val in enumerate(disk) if val is not None)
print(result)
