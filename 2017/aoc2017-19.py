import os

grid = []
with open(os.path.join('data', 'aoc19.txt')) as file:
    for line in file:
        grid.append(line.rstrip('\n'))

steps = 0
pos = (0, grid[0].find('|'))
direct = (1, 0)
letters = []
while True:
    my_pipe = '-' if direct[1] != 0 else '|'
    other_pipe = '|' if direct[1] != 0 else '-'

    cur = grid[pos[0]][pos[1]]
    ahead = (pos[0] + direct[0], pos[1] + direct[1])
    if cur == ' ':
        print(''.join(letters))
        print(steps)
        break

    steps += 1

    if cur.isalpha():
        letters.append(cur)
        pos = ahead
    elif cur in (my_pipe, other_pipe):
        pos = ahead
    elif cur == '+':
        if direct[0] != 0:
            ortho = (0, -1)
        else:
            ortho = (-1, 0)
        left = (pos[0] + ortho[0], pos[1] + ortho[1])
        if grid[left[0]][left[1]] != ' ':
            direct = ortho
            pos = left
        else:
            direct = (-ortho[0], -ortho[1])
            pos = (pos[0] + direct[0], pos[1] + direct[1])
