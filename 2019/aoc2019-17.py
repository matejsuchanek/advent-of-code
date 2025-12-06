import os

with open(os.path.join('data', 'aoc17.txt')) as file:
    data = file.read()

init = list(map(int, data.split(',')))

def read(address):
    prog.extend([0] * (address+1 - len(prog)))
    return prog[address]

def write(address, val):
    prog.extend([0] * (address+1 - len(prog)))
    prog[address] = val

inputs = []
out = []
prog = init[:]
pc = 0
base = 0
while True:
    inst = prog[pc]
    #print('%05d' % inst)
    params, opcode = divmod(inst, 100)
    a, b, c = params // 100, (params % 100) // 10, params % 10
    if opcode in (1, 2):
        if c == 1:
            x = prog[pc+1]
        else:
            offset = base if c == 2 else 0
            x = read(offset + prog[pc+1])
        if b == 1:
            y = prog[pc+2]
        else:
            offset = base if b == 2 else 0
            y = read(offset + prog[pc+2])
        val = x * y if opcode == 2 else x + y
        offset = base if a == 2 else 0
        write(offset + prog[pc+3], val)
        pc += 4
    elif opcode == 3:
        offset = base if c == 2 else 0
        write(offset + prog[pc+1], inputs.pop(0))
        pc += 2
    elif opcode == 4:
        if c == 1:
            val = prog[pc+1]
        else:
            offset = base if c == 2 else 0
            val = read(offset + prog[pc+1])
        out.append(val)
        pc += 2
    elif opcode in (5, 6):
        if c == 1:
            param = prog[pc+1]
        else:
            offset = base if c == 2 else 0
            param = read(offset + prog[pc+1])
        if (opcode == 6) is (param == 0):
            if b == 1:
                pc = prog[pc+2]
            else:
                offset = base if b == 2 else 0
                pc = read(offset + prog[pc+2])
        else:
            pc += 3
    elif opcode in (7, 8):
        if c == 1:
            first = prog[pc+1]
        else:
            offset = base if c == 2 else 0
            first = read(offset + prog[pc+1])
        if b == 1:
            second = prog[pc+2]
        else:
            offset = base if b == 2 else 0
            second = read(offset + prog[pc+2])
        if opcode == 8:
            val = 1 if first == second else 0
        else:
            val = 1 if first < second else 0
        offset = base if a == 2 else 0
        write(offset + prog[pc+3], val)
        pc += 4
    elif opcode == 9:
        if c == 1:
            base += prog[pc+1]
        else:
            offset = base if c == 2 else 0
            base += read(offset + prog[pc+1])
        pc += 2
    elif opcode == 99:
        break

grid = []
row = []
for c in map(chr, out):
    if c in '.#':
        row.append(c)
    elif row:
        grid.append(row)
        row = []

result = 0
for x, row in enumerate(grid):
    if 0 < x < (len(grid) - 1):
        for y, c in enumerate(row):
            if 0 < y < (len(row) - 1):
                if c == row[y-1] == row[y+1] == grid[x-1][y] == grid[x+1][y] == '#':
                    result += x * y

print(result)
