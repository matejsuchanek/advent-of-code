import os

program = []

with open(os.path.join('data', 'aoc8.txt')) as f:
    for line in f:
        instr, num = line.split()
        num = int(num.rstrip())
        program.append((instr, num))


def run(prog):
    index = 0
    already = set()
    acc = 0

    while index < len(prog):
        instr, num = prog[index]
        if index in already:
            return False, acc
        already.add(index)
        if instr == 'acc':
            acc += num
            index += 1
        elif instr == 'jmp':
            index += num
        else:
            index += 1
    return True, acc


print(run(program)[1])

for i, (instr, num) in enumerate(program):
    if instr in ('jmp', 'nop'):
        other = 'jmp' if instr == 'nop' else 'nop'
        copy = list(program)
        copy[i] = (other, num)
        res, acc = run(copy)
        if res:
            print(acc)
            break
