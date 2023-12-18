import os


class TheException(RuntimeError):
    pass


def run(job):
    if job == 'humn':
        raise TheException

    op = jobs[job]
    if len(op) == 1:
        return int(op[0])

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


jobs = {}
with open(os.path.join('data', 'aoc21.txt'), 'r') as file:
    for line in file:
        key, right = line.rstrip().split(': ')
        jobs[key] = right.split()

jobs['root'][1] = '='

key = 'root'
expect = None
while key != 'humn':
    left_job, op, right_job = jobs[key]
    left = right = None

    try:
        left = run(left_job)
    except TheException:
        pass

    try:
        right = run(right_job)
    except TheException:
        pass

    if left is None:
        key = left_job
    else:
        key = right_job

    value = left if left is not None else right
    if op == '=':
        expect = value
    elif op == '+':
        expect = expect - value
    elif op == '*':
        expect = expect // value
    elif op == '-':
        if left is None:
            expect += right
        else:
            expect = left - expect
    elif op == '/':
        if left is None:
            expect *= right
        else:
            expect = left // expect

print(expect)
