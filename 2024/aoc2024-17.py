import itertools
import os


def run(register, check=True):
    combo = lambda x: register[combo_to_reg[x]] if x in combo_to_reg else x

    ip = 0
    output = []

    length = len(program)
    while 0 <= ip < length:
        opcode = program[ip]
        operand = program[ip+1]

        jump = False
        if opcode == 0:
            register['A'] >>= combo(operand)
        elif opcode == 1:
            register['B'] ^= operand
        elif opcode == 2:
            register['B'] = combo(operand) & 0x7
        elif opcode == 3:
            if register['A'] != 0:
                ip = operand
                jump = True
        elif opcode == 4:
            register['B'] ^= register['C']
        elif opcode == 5:
            val = combo(operand) & 0x7
            if check and val != program[len(output)]:
                return None
            output.append(val)
        elif opcode == 6:
            register['B'] = register['A'] >> combo(operand)
        elif opcode == 7:
            register['C'] = register['A'] >> combo(operand)

        if not jump:
            ip += 2

    return output


combo_to_reg = {4: 'A', 5: 'B', 6: 'C'}
register = {}

with open(os.path.join('data', 'aoc17.txt')) as file:
    for char in 'ABC':
        register[char] = int(
            next(file)
            .removeprefix(f'Register {char}:')
            .strip()
        )

    next(file)
    program = list(
        map(int, next(file).removeprefix('Program:').strip().split(','))
    )

output = run(dict(register), check=False)
print(','.join(map(str, output)))
