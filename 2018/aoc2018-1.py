import os

with open(os.path.join('data', 'aoc1.txt')) as file:
    numbers = list(map(int, map(str.strip, file)))

print(sum(numbers))

freq = {0}
out = 0
stop = False
while not stop:
    for num in numbers:
        out += num
        if out in freq:
            print(out)
            stop = True
            break
        freq.add(out)
