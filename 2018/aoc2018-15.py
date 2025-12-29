import os
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Unit:

    pos: tuple[int, int]
    is_elf: bool
    hp: int = field(init=False)

    def __post_init__(self) -> None:
        self.hp = 200

    def hit(self, by=3) -> None:
        self.hp -= by

    @property
    def alive(self) -> bool:
        return self.hp > 0

    def copy(self) -> 'Unit':
        return Unit(self.pos, self.is_elf)


def around(pos):
    x, y = pos
    return {(x, y-1), (x, y+1), (x-1, y), (x+1, y)}


walls = set()
all_units = defaultdict(list)

with open(os.path.join('data', 'aoc15.txt')) as file:
    for i, line in enumerate(map(str.rstrip, file)):
        for j, c in enumerate(line):
            loc = (i, j)
            if c == '#':
                walls.add(loc)
            elif c in ('G', 'E'):
                all_units[c].append(Unit(loc, c == 'E'))

power = 3

while True:    
    goblins = [unit.copy() for unit in all_units['G']]
    elves = [unit.copy() for unit in all_units['E']]
    units = goblins + elves
    stop = False
    rounds = 0

    while True:
        for unit in sorted(units, key=lambda x: x.pos):
            if not unit.alive:
                continue

            enemies = goblins if unit.is_elf else elves
            enemies = [e for e in enemies if e.alive]
            if not enemies:
                stop = True
                break

            in_range = set()
            for e in enemies:
                in_range |= around(e.pos)
            in_range.discard(walls)

            if unit.pos not in in_range:
                in_range.discard(x.pos for x in units if x.alive)

                if not in_range:
                    continue

                queue = {unit.pos}
                already = walls | {x.pos for x in units if x.alive}
                while queue and not (queue & in_range):
                    already |= queue
                    new_queue = set()
                    for pos in queue:
                        new_queue |= around(pos)
                    queue = new_queue - already

                closest = queue & in_range
                if not closest:
                    continue

                target = min(closest)
                queue = {target}
                already = walls | {x.pos for x in units if x.alive}
                while not (around(unit.pos) & queue):
                    already |= queue
                    new_queue = set()
                    for pos in queue:
                        new_queue |= around(pos)
                    queue = new_queue - already

                unit.pos = min(queue & around(unit.pos))

            look = around(unit.pos)
            neighbors = [e for e in enemies if e.pos in look]
            if neighbors:
                victim = min(neighbors, key=lambda e: (e.hp, e.pos))
                victim.hit(3 if victim.is_elf else power)

        if stop:
            break

        rounds += 1

    total_hp = sum(unit.hp for unit in units if unit.alive)
    if power == 3:
        print(total_hp * rounds)

    if all(unit.alive for unit in elves):
        print(total_hp * rounds)
        break

    power += 1
