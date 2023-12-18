import os

jobs = {}


def run(job):
    op = jobs[job]
    if len(op) == 1:
        return cache[job]

    left = run(op[0])
    right = run(op[2])
    if op[1] == '+':
        return left + right
    elif op[1] == '-':
        return left - right
    elif op[1] == '*':
        return left * right
    elif op[1] == '/':
        return left // right


with open(os.path.join('data', 'aoc21.txt'), 'r') as file:
    for line in file:
        key, right = line.rstrip().split(': ')
        jobs[key] = right.split()

print(run('root'))
