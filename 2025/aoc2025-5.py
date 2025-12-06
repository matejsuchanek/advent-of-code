import os

ranges = []
fresh = 0

with open(os.path.join('data', 'aoc5.txt')) as file:
    for line in file:
        line = line.rstrip()
        if not line:
            break

        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    for ingr in map(int, file):
        fresh += any(
            start <= ingr <= end
            for start, end in ranges
        )

print(fresh)

ranges.sort()

merged = []

last_start, last_end = ranges[0]
for start, end in ranges:
    if start > last_end:
        merged.append((last_start, last_end))
        last_start, last_end = start, end
    else:
        last_end = max(last_end, end)

merged.append((last_start, last_end))

total = sum(end - start + 1 for start, end in merged)
print(total)
