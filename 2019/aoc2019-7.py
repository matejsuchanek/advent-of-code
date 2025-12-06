from itertools import permutations
from math import inf

with open(os.path.join('data', 'aoc7.txt')) as file:
    data = file.read()

init = list(map(int, data.split(',')))

def run(prog, inputs):
    pc = 0
    inputs = iter(inputs)
    while True:
        inst = prog[pc]
        params, opcode = divmod(inst, 100)
        _, b, c = params // 100, (params % 100) // 10, params % 10
        if opcode in (1, 2):
            if c == 1:
                x = prog[pc+1]
            else:
                x = prog[prog[pc+1]]
            if b == 1:
                y = prog[pc+2]
            else:
                y = prog[prog[pc+2]]
            val = x * y if opcode == 2 else x + y
            prog[prog[pc+3]] = val
            pc += 4
        elif opcode == 3:
            prog[prog[pc+1]] = next(inputs)
            pc += 2
        elif opcode == 4:
            if c == 1:
                val = prog[pc+1]
            else:
                val = prog[prog[pc+1]]
            out = val
            pc += 2
        elif opcode in (5, 6):
            if c == 1:
                param = prog[pc+1]
            else:
                param = prog[prog[pc+1]]
            if (opcode == 6) is (param == 0):
                if b == 1:
                    pc = prog[pc+2]
                else:
                    pc = prog[prog[pc+2]]
            else:
                pc += 3
        elif opcode in (7, 8):
            if c == 1:
                first = prog[pc+1]
            else:
                first = prog[prog[pc+1]]
            if b == 1:
                second = prog[pc+2]
            else:
                second = prog[prog[pc+2]]
            if opcode == 8:
                val = 1 if first == second else 0
            else:
                val = 1 if first < second else 0
            prog[prog[pc+3]] = val
            pc += 4
        elif opcode == 99:
            break

    return out


result = -inf
for setting in permutations(range(5)):
    out = 0
    for phase in setting:
        out = run(init[:], [phase, out])
    result = max(result, out)

print(result)
