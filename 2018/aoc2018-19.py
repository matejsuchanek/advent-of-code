import os


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

prog = []

with open(os.path.join('data', 'aoc19.txt')) as file:
    bound = int(next(file)[4])
    for line in map(str.rstrip, file):
        instr, *values = line.split()
        prog.append([instr] + [int(x) for x in values])

for reg_zero in (0, 1):
    regs = [0] * 6
    regs[0] = reg_zero
    ip = 0
    while 0 <= ip < len(prog):
        instr, *values = prog[ip]
        regs[bound] = ip
        codes[instr](*values, regs)
        ip = regs[bound] + 1

    print(regs[0])
