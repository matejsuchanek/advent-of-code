import os

def matches(line, nonterms):
    if line == '' or nonterms == []:
        return line == '' and nonterms == []

    first = nonterms[0]
    rules = grammar[first]
    if isinstance(rules, str):
        if line.startswith(rules):
            return matches(line[1:], nonterms[1:])
        else:
            return False

    for subst in grammar[first]:
        ok = matches(line, subst + nonterms[1:])
        if ok:
            return True

    return False


grammar = {}

with open(os.path.join('data', 'aoc19.txt')) as f:
    for line in f:
        if not line.rstrip():
            break
        left, right = line.rstrip().split(': ')
        if right.startswith('"') and right.endswith('"'):
            grammar[int(left)] = right[1:-1]
        else:
            grammar[int(left)] = []
            for rule in right.split(' | '):
                grammar[int(left)].append([int(x) for x in rule.split()])

    lines = []
    for line in f:
        lines.append(line.rstrip())

total = 0
for line in lines:
    total += matches(line, [0])

print(total)

grammar[8][:] = [[42], [42, 8]]
grammar[11][:] = [[42, 31], [42, 11, 31]]

total = 0
for line in lines:
    total += matches(line, [0])

print(total)
