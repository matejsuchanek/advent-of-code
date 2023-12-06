import math
import os

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
        expr = line.removeprefix('Operation: ')

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

for _ in range(20):
    for m in order:
        data = monkeys[m]
        for item in data['items']:
            business[m] += 1
            loc = {'old': item}
            exec(data['expr'], {}, loc)
            new = loc['new'] // 3
            if new % data['div'] == 0:
                monkeys[data['if_true']]['items'].append(new)
            else:
                monkeys[data['if_false']]['items'].append(new)
        data['items'] = []

print(math.prod(sorted(business.values())[-2:]))
