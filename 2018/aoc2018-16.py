import os

def get_line_as_ints(text):
    text = text[text.index('[')+1:text.index(']')]
    return [int(x) for x in text.split(', ')]


def change_reg(regs, i, val):
    regs[i] = val


codes = {
    'addr': lambda a, b, c, regs: change_reg(regs, c, regs[a] + regs[b]),
    'addi': lambda a, b, c, regs: change_reg(regs, c, regs[a] + b),
    'mulr': lambda a, b, c, regs: change_reg(regs, c, regs[a] * regs[b]),
    'muli': lambda a, b, c, regs: change_reg(regs, c, regs[a] * b),
    'banr': lambda a, b, c, regs: change_reg(regs, c, regs[a] & regs[b]),
    'bani': lambda a, b, c, regs: change_reg(regs, c, regs[a] & b),
    'borr': lambda a, b, c, regs: change_reg(regs, c, regs[a] | regs[b]),
    'bori': lambda a, b, c, regs: change_reg(regs, c, regs[a] | b),
    'setr': lambda a, b, c, regs: change_reg(regs, c, regs[a]),
    'seti': lambda a, b, c, regs: change_reg(regs, c, a),
    'gtir': lambda a, b, c, regs: change_reg(regs, c, int(a > regs[b])),
    'gtri': lambda a, b, c, regs: change_reg(regs, c, int(regs[a] > b)),
    'gtrr': lambda a, b, c, regs: change_reg(regs, c, int(regs[a] > regs[b])),
    'eqir': lambda a, b, c, regs: change_reg(regs, c, int(a == regs[b])),
    'eqri': lambda a, b, c, regs: change_reg(regs, c, int(regs[a] == b)),
    'eqrr': lambda a, b, c, regs: change_reg(regs, c, int(regs[a] == regs[b])),
}
can_be = {code: set(range(16)) for code in codes}

at_least_three = 0

with open(os.path.join('data', 'aoc16.txt')) as file:
    while True:
        line = next(file).strip()
        if not line.startswith('Before:'):
            break
        before = get_line_as_ints(line)
        opcode, *abc = map(int, next(file).split())
        after = get_line_as_ints(next(file))
        next(file)  # empty
        count = 0
        for key, cb in codes.items():
            regs = before[:]
            cb(*abc, regs)
            if regs == after:
                count += 1
            elif opcode in can_be[key]:
                can_be[key].remove(opcode)
        if count >= 3:
            at_least_three += 1
    print(at_least_three)

    assigned = {}
    while can_be:
        singles = {key for key, value in can_be.items() if len(value) == 1}
        for key in singles:
            opc = can_be.pop(key).pop()
            assigned[opc] = key
            for key, values in can_be.items():
                if opc in values:
                    values.remove(opc)

    next(file)  # empty
    regs = [0] * 4
    for line in file:
        opcode, *abc = map(int, line.split())
        codes[assigned[opcode]](*abc, regs)
    print(regs[0])
