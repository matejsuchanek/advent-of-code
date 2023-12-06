import math
import os

def func(op, right):
    if right == 'old':
        if op == '*':
            return lambda old: old * old
        else:
            return lambda old: old + old
    else:
        right = int(right)
        if op == '*':
            return lambda old: old * right
        else:
            return lambda old: old + right


monkeys = {}
order = []

with open(os.path.join('data', 'aoc11.txt'), 'r') as file:
    it = map(str.rstrip, file)

    while True:
        line = next(it)
        m = line.removeprefix('Monkey ').removesuffix(':')
        order.append(m)

        line = next(it).lstrip()
        items = line.removeprefix('Starting items: ').split(', ')
        items = [int(n) for n in items]

        line = next(it).lstrip()
        raw_expr = line.removeprefix('Operation: new = ')
        expr = func(*raw_expr.split()[1:])

        line = next(it).lstrip()
        div = int(line.removeprefix('Test: divisible by '))

        line = next(it).lstrip()
        if_true = line.removeprefix('If true: throw to monkey ')

        line = next(it).lstrip()
        if_false = line.removeprefix('If false: throw to monkey ')

        monkeys[m] = {
            'items': items,
            'expr': expr,
            'div': div,
            'if_true': if_true,
            'if_false': if_false,
        }

        if next(it, None) is None:
            break

business = dict.fromkeys(order, 0)
div = math.prod(d['div'] for d in monkeys.values())

for i in range(10_000):
    for m in order:
        data = monkeys[m]
        for item in data['items']:
            business[m] += 1
            new = data['expr'](item) % div
            if new % data['div'] == 0:
                monkeys[data['if_true']]['items'].append(new)
            else:
                monkeys[data['if_false']]['items'].append(new)
        data['items'] = []

print(math.prod(sorted(business.values())[-2:]))
