import os

half = total = 0

with open(os.path.join('data', 'aoc2.txt')) as file:
    line = next(file)

for interval in line.rstrip().split(','):
    start, end = interval.split('-')
    for num in range(int(start), int(end) + 1):
        s = str(num)
        length = len(s)

        add_half = add_total = False
        for size in range(1, 1 + length // 2):
            div, mod = divmod(length, size)
            if mod > 0:
                continue

            sub = s[:size]
            if all(
                s[i*size:(i+1)*size] == sub
                for i in range(1, div)
            ):
                add_total = True
                if div == 2:
                    add_half = True
                    break

        if add_half:
            half += num
        if add_total:
            total += num

print(half)
print(total)
