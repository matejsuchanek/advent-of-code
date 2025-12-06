import os
from collections import deque
from heapq import *


class Bot:
    def __init__(self, prog):
        self.prog = prog
        self.pc = 0
        self.base = 0

    def read(self, address):
        self.prog.extend([0] * (address+1 - len(self.prog)))
        return self.prog[address]

    def write(self, address, val):
        self.prog.extend([0] * (address+1 - len(self.prog)))
        self.prog[address] = val

    def run(self, inp):
        pc, base = self.pc, self.base
        prog = self.prog
        out = None
        while True:
            inst = prog[pc]
            params, opcode = divmod(inst, 100)
            a, b, c = params // 100, (params % 100) // 10, params % 10
            if opcode in (1, 2):
                if c == 1:
                    x = prog[pc+1]
                else:
                    offset = base if c == 2 else 0
                    x = self.read(offset + prog[pc+1])
                if b == 1:
                    y = prog[pc+2]
                else:
                    offset = base if b == 2 else 0
                    y = self.read(offset + prog[pc+2])
                val = x * y if opcode == 2 else x + y
                offset = base if a == 2 else 0
                self.write(offset + prog[pc+3], val)
                pc += 4
            elif opcode == 3:
                offset = base if c == 2 else 0
                self.write(offset + prog[pc+1], inp)
                pc += 2
            elif opcode == 4:
                if c == 1:
                    val = prog[pc+1]
                else:
                    offset = base if c == 2 else 0
                    val = self.read(offset + prog[pc+1])
                out = val
                pc += 2
                break
            elif opcode in (5, 6):
                if c == 1:
                    param = prog[pc+1]
                else:
                    offset = base if c == 2 else 0
                    param = self.read(offset + prog[pc+1])
                if (opcode == 6) is (param == 0):
                    if b == 1:
                        pc = prog[pc+2]
                    else:
                        offset = base if b == 2 else 0
                        pc = self.read(offset + prog[pc+2])
                else:
                    pc += 3
            elif opcode in (7, 8):
                if c == 1:
                    first = prog[pc+1]
                else:
                    offset = base if c == 2 else 0
                    first = self.read(offset + prog[pc+1])
                if b == 1:
                    second = prog[pc+2]
                else:
                    offset = base if b == 2 else 0
                    second = self.read(offset + prog[pc+2])
                if opcode == 8:
                    val = 1 if first == second else 0
                else:
                    val = 1 if first < second else 0
                offset = base if a == 2 else 0
                self.write(offset + prog[pc+3], val)
                pc += 4
            elif opcode == 9:
                if c == 1:
                    base += prog[pc+1]
                else:
                    offset = base if c == 2 else 0
                    base += self.read(offset + prog[pc+1])
                pc += 2
            elif opcode == 99:
                break

        self.pc, self.base = pc, base
        return out


def around(pos):
    for dx, dy in moves.values():
        yield (pos[0] + dx, pos[1] + dy)


def around_unvisited(pos):
    for new in around(pos):
        if new not in plan:
            yield new


def bfs(start, end):
    heap = [(0, start)]
    already = set()
    prev = {}
    while True:
        d, pos = heappop(heap)
        if pos == end:
            break
        if pos in already:
            continue
        already.add(pos)
        for loc in around(pos):
            if plan.get(pos) == 1 or pos == end:
                if loc not in already:
                    heappush(heap, (d + 1, loc))
                    prev[loc] = pos

    path = deque()
    node = end
    while node in prev:
        path.appendleft(node)
        node = prev[node]
    return path


def move_to_and_backtrack(bot, pos, target):
    path = bfs(pos, target)
    history = []
    while path:
        node = path.popleft()
        diff = (node[0] - pos[0], node[1] - pos[1])
        d = dirs[diff]
        status = bot.run(d)
        pos = node
        if pos != target:
            assert status != 0
        if status != 0:
            history.append(d)
    for d in reversed(history):
        assert bot.run(opposite[d]) != 0
    return status


NORTH, SOUTH, WEST, EAST = range(1, 5)
moves = {
    NORTH: (0, 1),
    SOUTH: (0, -1),
    WEST: (-1, 0),
    EAST: (1, 0),
}
dirs = {v: d for d, v in moves.items()}
opposite = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    WEST: EAST,
    EAST: WEST,
}

with open(os.path.join('data', 'aoc15.txt')) as file:
    line = next(file)
    prog = list(map(int, line.split(',')))

bot = Bot(prog)
pos = (0, 0)
plan = {pos: 1}
queue = deque(moves.values())
step = 0
while queue:
    target = queue.popleft()
    status = move_to_and_backtrack(bot, pos, target)
    if status == 2:
        path = bfs(pos, target)
        print(len(path))
    plan[target] = status
    if status != 0:
        queue.extend(around_unvisited(target))

location = {loc for loc, stat in plan.items() if stat == 2}.pop()
queue = [location]
already = {location}
minute = 0
while queue:
    new = []
    for loc in queue:
        for adj in around(loc):
            if plan[adj] == 1 and adj not in already:
                new.append(adj)
                already.add(loc)
    queue = new
    if queue:
        minute += 1

print(minute)
