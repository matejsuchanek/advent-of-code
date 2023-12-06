import os


class Position:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other) -> 'Position':
        return Position(self.x + other[0], self.y + other[1])

    def __iadd__(self, other) -> 'Position':
        return Position(self.x + other[0], self.y + other[1])

    def is_adjacent(self, other: 'Position') -> bool:
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    @property
    def tuple(self):
        return (self.x, self.y)


class Knot:

    diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def __init__(self, pos, next_=None) -> None:
        self.pos = Position(*pos)
        self.next = next_

    def is_adjacent_to_next(self) -> bool:
        return self.pos.is_adjacent(self.next.pos)

    def move(self, move) -> None:
        self.pos += move

    def follow(self) -> bool:
        if self.is_adjacent_to_next():
            return False
        if self.pos.x != self.next.pos.x \
           and self.pos.y != self.next.pos.y:
            moves = self.diag
        else:
            moves = dirs.values()
        for move in moves:
            new = self.pos + move
            if self.next.pos.is_adjacent(new):
                self.move(move)
                return True


lines = []
with open(os.path.join('data', 'aoc9.txt'), 'r') as file:
    lines.extend(map(str.split, file))

head = Knot((0, 0))
tail = Knot((0, 0), head)
dirs = {
    'R': (+1, 0),
    'L': (-1, 0),
    'U': (0, +1),
    'D': (0, -1),
}
visited = {tail.pos.tuple}

for d, steps in lines:
    steps = int(steps)
    move = dirs[d]
    for _ in range(steps):
        head.move(move)
        if tail.follow():
            visited.add(tail.pos.tuple)

print(len(visited))

head = Knot((0, 0))
knots = []
next_ = head
for i in range(9):
    the_knot = Knot((0, 0), next_)
    knots.append(the_knot)
    next_ = the_knot
del next_

visited = {knots[-1].pos.tuple}

for d, steps in lines:
    steps = int(steps)
    move = dirs[d]
    for _ in range(steps):
        head.move(move)
        for knot in knots:
            if not knot.follow():
                break
        else:
            visited.add(knots[-1].pos.tuple)

print(len(visited))
