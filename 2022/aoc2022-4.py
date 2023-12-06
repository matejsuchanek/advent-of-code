import os

total = overlap = 0
with open(os.path.join('data', 'aoc4.txt'), 'r') as file:
    for line in map(str.strip, file):
        first, second = [[int(n) for n in x.split('-')]
                         for x in line.split(',')]
        if second[0] <= first[0] and first[1] <= second[1]:
            total += 1
        elif first[0] <= second[0] and second[1] <= first[1]:
            total += 1

        if first[0] <= second[0] <= first[1]:
            overlap += 1
        elif first[0] <= second[1] <= first[1]:
            overlap += 1
        elif second[0] <= first[0] <= second[1]:
            overlap += 1
        elif second[0] <= first[1] <= second[1]:
            overlap += 1

print(total)
print(overlap)
