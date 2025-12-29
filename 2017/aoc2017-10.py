import os

with open(os.path.join('data', 'aoc10.txt')) as file:
    string = next(file).rstrip()

lengths = list(map(int, string.split(',')))

l = list(range(256))
pos = 0
skip = 0

for length in lengths:
    if length <= len(l):
        end = (pos + length - 1) % len(l)
        if length > 1:
            stack = []
            while True:
                stack.append(l[end])
                if pos == end:
                    break
                if end == 0:
                    end = len(l)
                end -= 1
            for i, val in enumerate(stack, pos):
                l[i % len(l)] = val
        pos = (pos + length + skip) % len(l)
    skip += 1

print(l[0] * l[1])
