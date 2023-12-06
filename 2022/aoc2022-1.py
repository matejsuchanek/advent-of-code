import os

elves = []
with open(os.path.join('data', 'aoc1.txt'), 'r') as file:
    this = 0
    for line in map(str.strip, file):
        if line == '':
            elves.append(this)
            this = 0
        else:
            this += int(line)
    elves.append(this)

print(max(elves))
print(sum(sorted(elves)[-3:]))
