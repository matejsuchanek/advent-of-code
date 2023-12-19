import math
import os
import re
from dataclasses import dataclass


def do_one(parts, name):
    for cond in workflows[name]:
        if isinstance(cond, str):
            return cond
        c, op, val, dest = cond
        if op == '>' and parts[c] > val:
            return dest
        if op == '<' and parts[c] < val:
            return dest
    raise RuntimeError


@dataclass(frozen=True)
class Interval:

    lb: int
    ub: int

    def split(self, op, val):
        if op == '<':
            if self.ub < val:
                return self, None
            elif self.lb < val:
                return Interval(self.lb, val - 1), Interval(val, self.ub)
            else:
                return None, self
        if op == '>':
            if val < self.lb:
                return self, None
            elif val < self.ub:
                return Interval(val + 1, self.ub), Interval(self.lb, val)
            else:
                return None, self

    @property
    def size(self):
        return self.ub - self.lb + 1


def make_copy(parts):
    return {k: val for k, val in parts.items()}


def dfs(parts, name):
    out = 0
    for cond in workflows[name]:
        if cond == 'R':
            continue
        if cond == 'A':
            out += math.prod([inter.size for inter in parts.values()])
            continue
        if isinstance(cond, str):
            out += dfs(parts, cond)
            continue

        c, op, val, dest = cond
        sat, non_sat = parts[c].split(op, val)
        if sat and dest != 'R':
            copy = make_copy(parts)
            copy[c] = sat
            if dest == 'A':
                out += math.prod([inter.size for inter in copy.values()])
            else:
                out += dfs(copy, dest)

        if not non_sat:
            break

        parts = make_copy(parts)
        parts[c] = non_sat

    return out


regex = re.compile(r'([a-z]+)\{([^}]+)\}')
workflows = {}
prim = 0

with open(os.path.join('data', 'aoc19.txt'), 'r') as file:
    for line in file:
        line = line.rstrip()
        if not line:
            break

        match = regex.match(line)
        name = match[1]
        workflows[name] = []
        for step in match[2].split(','):
            if ':' in step:
                cond, dest = step.split(':', 1)
                workflows[name].append((cond[0], cond[1], int(cond[2:]), dest))
            else:
                workflows[name].append(step)

    for line in file:
        data = {}
        for x in line.rstrip()[1:-1].split(','):
            c, val = x.split('=', 1)
            data[c] = int(val)

        name = 'in'
        while name not in ('A', 'R'):
            name = do_one(data, name)
        if name == 'A':
            prim += sum(data.values())

print(prim)

init = {c: Interval(1, 4000) for c in 'xmas'}
sec = dfs(init, 'in')
print(sec)
