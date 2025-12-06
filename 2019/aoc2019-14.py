data = {}

with open(os.path.join('data', 'aoc14.txt')) as file:
    for line in file:
        left, right = line.strip().split(' => ', 2)
        i, out = right.split(' ')
        inputs = []
        for ingr in left.split(', '):
            n, what = ingr.split(' ')
            inputs.append((int(n), what))
        data[out] = (int(i), inputs)


def get_ORE(num, what, leftover):
    if what == 'ORE':
        return num
    c, inputs = data[what]
    div, mod = divmod(num, c)
    times = div + (mod > 0)
    out = 0
    for n, chem in inputs:
        need = times * n
        if chem in leftover:
            if leftover[chem] > need:
                leftover[chem] -= need
                need = 0
            else:
                need -= leftover.pop(chem)
        if need == 0:
            continue
        out += get_ORE(need, chem, leftover)
    over = (times * c) - num
    if over:
        leftover[what] = over
    return out


print(get_ORE(1, 'FUEL', {}))

ore = 10**12
step = 1000
f = step
while True:
    need = get_ORE(f, 'FUEL', {})
    if need > ore:
        for j in range(f - step + 1, f):
            need = get_ORE(j, 'FUEL', {})
            if need > ore:
                print(j-1)
                break
        else:
            print(f-1)
        break
    f += step

