import os

with open(os.path.join('data', 'aoc6.txt')) as file:
    blocks = [int(val) for val in next(file).split()]

length = len(blocks)

cycles = 0
prev = []
prev.append(list(blocks))
starting = -1
while True:
    cycles += 1
    index = 0
    for i in range(length):
        if blocks[index] < blocks[i]:
            index = i
    left = blocks[index]
    blocks[index] = 0
    while left:
        index = (index + 1) % length
        blocks[index] += 1
        left -= 1
    for i, data in enumerate(prev):
        if data == blocks:
            starting = i
    if starting > -1:
        break
    prev.append(list(blocks))

print(cycles)
print(cycles - starting)
