import os

def get_population(lines, pos):
    return sum(line[pos] == '1' for line in lines)


def get_counts(lines):
    length = len(lines[0])
    return [get_population(lines, i) for i in range(length)]


def select(lines, pos, val):
    return [line for line in lines if line[pos] == val]


lines = []
with open(os.path.join('data', 'aoc3.txt'), 'r') as file:
    for line in file:
        lines.append(line.rstrip())

count = len(lines)
ones = get_counts(lines)
gamma = eps = ''
for n in ones:
    if n > (count // 2):
        gamma += '1'
        eps += '0'
    else:
        gamma += '0'
        eps += '1'

print(int(gamma, 2) * int(eps, 2))

oxy = [line for line in lines]
co2 = [line for line in lines]
for i in range(len(ones)):
    count = len(oxy)
    if count > 1:
        num = get_population(oxy, i)
        if num < count / 2:
            oxy = select(oxy, i, '0')
        else:
            oxy = select(oxy, i, '1')

    count = len(co2)
    if count > 1:
        num = get_population(co2, i)
        if num < count / 2:
            co2 = select(co2, i, '1')
        else:
            co2 = select(co2, i, '0')

assert len(oxy) == 1
assert len(co2) == 1
print(int(oxy[0], 2) * int(co2[0], 2))
