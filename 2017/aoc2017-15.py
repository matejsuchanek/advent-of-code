import os
import re

lineR = re.compile(r'Generator [AB] starts with (\d+)')

with open(os.path.join('data', 'aoc15.txt')) as file:
    a = int(lineR.match(next(file)).group(1))
    b = int(lineR.match(next(file)).group(1))

result = 0

for _ in range(40_000_000):
    a = (a * 16_807) % 2_147_483_647
    b = (b * 48_271) % 2_147_483_647
    my_a, my_b = a, b
    for _ in range(16):
        my_a, mod_a = divmod(my_a, 2)
        my_b, mod_b = divmod(my_b, 2)
        if mod_a != mod_b:
            break
    else:
        result += 1

print(result)
