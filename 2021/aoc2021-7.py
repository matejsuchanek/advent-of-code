import os

crabs = []
with open(os.path.join('data', 'aoc7.txt'), 'r') as file:
    line = next(file)
    crabs.extend(int(n) for n in line.split(','))

start = min(crabs)
stop = max(crabs)

best_const = 2**31
best = 2**31
for i in range(start, stop + 1):
    this = sum(abs(i - n) for n in crabs)
    if this < best_const:
        best_const = this

    this = 0
    for n in crabs:
        dist = abs(n - i)
        this += (dist * (dist + 1)) // 2
    if this < best:
        best = this

print(best_const)
print(best)
