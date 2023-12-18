import os

groups = []
with open(os.path.join('data', 'aoc6.txt')) as f:
    group = []
    for line in f:
        line = line.rstrip()
        if line:
            group.append(line)
        else:
            groups.append(group)
            group = []
    if group:
        groups.append(group)

anyone = everyone = 0
for group in groups:
    anyone += len(set(''.join(group)))
    common = set(group[0]).intersection(*group)
    everyone += len(common)
print(anyone)
print(everyone)
