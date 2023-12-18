import os
import re

from collections import deque

mask = ['X'] * 36
regex = re.compile(r'mem\[(\d+)\] = (\d+)')
memory = {}

with open(os.path.join('data', 'aoc14.txt')) as f:
    for line in f:
        if line.startswith('mask ='):
            mask = list(line[7:43])
        else:
            match = regex.fullmatch(line.rstrip())
            pos, value = match.groups()

            pos = int(pos)
            bits = []
            while pos:
                pos, rem = divmod(pos, 2)
                bits.append(rem)
            bits.extend([0] * (36 - len(bits)))
            bits[:] = bits[::-1]

            for i, bit in enumerate(mask):
                if bit == '1':
                    bits[i] = 1
                elif bit == 'X':
                    bits[i] = 'X'

            queue = deque()
            queue.append(bits)
            while queue:
                bits = queue.popleft()
                if 'X' in bits:
                    index = bits.index('X')
                    queue.append(bits[:index] + [0] + bits[index+1:])
                    queue.append(bits[:index] + [1] + bits[index+1:])
                    continue

                pos = 0
                power = 1
                for bit in reversed(bits):
                    pos += int(bit) * power
                    power *= 2
                memory[pos] = int(value)

print(sum(memory.values()))
