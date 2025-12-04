import os

cur = 50
zero = total = 0

sign = {'L': -1, 'R': 1}

with open(os.path.join('data', 'aoc1.txt')) as file:
    for line in file:
        first, num = line[0], int(line[1:].rstrip())

        incr, mod = divmod(num, 100)
        new = cur + sign[first] * mod
        if new > 99 or new == 0 or (new < 1 and cur != 0):
            incr += 1
        cur = new % 100
        total += incr
        zero += cur == 0

print(zero)
print(total)
