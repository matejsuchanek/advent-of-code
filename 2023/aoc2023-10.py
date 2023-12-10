import os
from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other) -> 'Position':
        dx, dy = other
        return Position(self.x + dx, self.y + dy)

    def inside(self, grid):
        return 0 <= self.x < len(grid) and 0 <= self.y < len(grid[self.x])

    def on_border(self, grid):
        return self.x == 0 or self.x == len(grid) - 1 \
               or self.y == 0 or self.y == len(grid[self.x]) - 1

    def get(self, grid):
        return grid[self.x][self.y]


up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

navig = {
    # ('pipe', move) -> (next_move, [right_hand])
    ('F', up): (right, []),
    ('F', left): (down, [up, left]),
    ('J', right): (up, [down, right]),
    ('J', down): (left, []),
    ('L', down): (right, [left, down]),
    ('L', left): (up, []),
    ('7', up): (left, [right, up]),
    ('7', right): (down, []),
    ('-', right): (right, [down]),
    ('-', left): (left, [up]),
    ('|', down): (down, [left]),
    ('|', up): (up, [right]),
}

grid = []

start = None

with open(os.path.join('data', 'aoc10.txt'), 'r') as file:
    for i, line in enumerate(file):
        grid.append(line.rstrip())
        if not start and 'S' in line:
            start = Position(i, line.index('S'))

assert start
next_move = None
for move in (down, up, right, left):
    node = start + move
    if not node.inside(grid):
        continue
    pipe = node.get(grid)
    if (pipe, move) in navig:
        next_move, _ = navig[pipe, move]
        break

loop = set()
right_hand = set()
pos = start

while True:
    loop.add(pos)
    pos += next_move
    pipe = pos.get(grid)
    if pipe == 'S':
        break
    next_move, look_at = navig[pipe, next_move]
    for move in look_at:
        node = pos + move
        if node.inside(grid):
            right_hand.add(node)

print(len(loop) // 2)

right_hand -= loop
queue = deque(right_hand)
while queue:
    node = queue.popleft()
    for move in (down, up, right, left):
        next_ = node + move
        if next_.inside(grid) \
           and next_ not in loop \
           and next_ not in right_hand:
            right_hand.add(next_)
            queue.append(next_)

if any(node.on_border(grid) for node in right_hand):
    inside = len(grid) * len(grid[0]) - len(loop) - len(right_hand)
else:
    inside = len(right_hand)

print(inside)
