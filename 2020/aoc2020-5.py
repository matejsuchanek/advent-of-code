import os

seats = set()
with open(os.path.join('data', 'aoc5.txt')) as f:
    for line in f:
        lower, upper = (0, 127)
        for c in line[:7]:
            size = (upper - lower) // 2
            if c == 'F':
                lower, upper = (lower, lower + size)
            elif c == 'B':
                lower, upper = (upper - size, upper)
        assert lower == upper
        row = lower

        lower, upper = (0, 7)
        for c in line[7:10]:
            size = (upper - lower) // 2
            if c == 'L':
                lower, upper = (lower, lower + size)
            elif c == 'R':
                lower, upper = (upper - size, upper)
        assert lower == upper
        seat = lower

        seats.add(row * 8 + seat)

top = max(seats)
start = min(seats)
print(top)
for i in range(start, top):
    if i not in seats and {i-1, i+1} <= seats:
        print(i)
        break
