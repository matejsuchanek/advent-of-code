import os
import re

mask = ['X'] * 36
regex = re.compile(r'mem\[(\d+)\] = (\d+)')
memory = {}

with open(os.path.join('data', 'aoc14.txt')) as f:
    for line in f:
        if line.startswith('mask ='):
            mask = list(line[7:43])
            assert len(mask) == 36
        else:
            match = regex.fullmatch(line.rstrip())
            pos, value = match.groups()
            value = int(value)
            bits = []
            while value:
                value, rem = divmod(value, 2)
                bits.append(rem)
            bits.extend([0] * (36 - len(bits)))
            bits[:] = bits[::-1]
            for i, bit in enumerate(mask):
                if bit != 'X':
                    bits[i] = bit

            value = 0
            power = 1
            for bit in reversed(bits):
                value += int(bit) * power
                power *= 2
            memory[int(pos)] = value

print(sum(memory.values()))
