import os

with open(os.path.join('data', 'aoc5.txt')) as file:
    init = [int(line) for line in map(str.rstrip, file)]

maze = init[:]
length = len(maze)
steps = 0
index = 0
while index < length:
    new_index = index + maze[index]
    maze[index] += 1
    index = new_index
    steps += 1

print(steps)

maze = init[:]
steps = 0
index = 0
while index < length:
    cur = maze[index]
    new_index = index + cur
    if cur >= 3:
        maze[index] -= 1
    else:
        maze[index] += 1
    index = new_index
    steps += 1

print(steps)
