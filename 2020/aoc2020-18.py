import os
import re


def evaluate_simple(expr):
    tokens = expr.split(' ')
    value = int(tokens[0])
    while len(tokens) >= 3:
        _, op, right = tokens[:3]
        tokens[:] = tokens[2:]
        if op == '+':
            value += int(right)
        elif op == '*':
            value *= int(right)

    return value


def evaluate_expr(line):
    while True:
        line, n = regex.subn(lambda m: str(evaluate_simple(m.group(1))), line)
        if n == 0:
            break
    return evaluate_simple(line)


regex = re.compile(r'\(([^()]+)\)')
result = 0

with open(os.path.join('data', 'aoc18.txt')) as f:
    for line in f:
        result += evaluate_expr(line.rstrip())

print(result)
