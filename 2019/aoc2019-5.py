import os

with open(os.path.join('data', 'aoc5.txt')) as file:
    data = file.read()

init = list(map(int, data.split(',')))

for out in (1, 5):
    prog = init[:]
    pc = 0
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
            prog[prog[pc+1]] = out
            pc += 2
        elif opcode == 4:
            if c == 1:
                out = prog[pc+1]
            else:
                out = prog[prog[pc+1]]
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
    
    print(out)
