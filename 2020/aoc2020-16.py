import os

constr = {}
rate = 0
nearby = []
ticket = None

with open(os.path.join('data', 'aoc16.txt')) as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            break

        field, _, ranges = line.partition(': ')
        constr[field] = []
        for rng in ranges.split(' or '):
            lower, upper = map(int, rng.split('-'))
            constr[field].append((lower, upper))

    if next(f).startswith('your ticket:'):
        ticket = tuple(map(int, next(f).rstrip().split(',')))

    line = next(f)
    if next(f).startswith('nearby tickets:'):
        for line in f:
            tpl = tuple(map(int, line.rstrip().split(',')))
            this_rate = 0
            for frag in tpl:
                if not any(
                    any(lb <= frag <= ub for (lb, ub) in rngs)
                    for rngs in constr.values()
                ):
                    this_rate += frag
            if this_rate:
                rate += this_rate
            else:
                nearby.append(tpl)

print(rate)

cols = len(nearby[0])
f_to_possible_c = {}

for field, rngs in constr.items():
    columns = []
    f_to_possible_c[field] = columns
    for col in range(cols):
        if all(
            any(lb <= tick[col] <= ub for (lb, ub) in rngs)
            for tick in nearby
        ):
            columns.append(col)

fields = {}

while f_to_possible_c:
    keys = {key for key, x in f_to_possible_c.items() if len(x) == 1}
    for field in keys:
        c = f_to_possible_c.pop(field).pop()
        fields[field] = c
        for value in f_to_possible_c.values():
            if c in value:
                value.remove(c)

prod = 1
for field, col in fields.items():
    if field.startswith('departure'):
        prod *= ticket[col]
print(prod)
