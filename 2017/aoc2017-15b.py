import os
import re


def make_gen(num, factor, base):
    while True:
        num = (num * factor) % 2_147_483_647
        if num % base == 0:
            yield num


lineR = re.compile(r'Generator [AB] starts with (\d+)')

with open(os.path.join('data', 'aoc15.txt')) as file:
    a = int(lineR.match(next(file)).group(1))
    b = int(lineR.match(next(file)).group(1))

result = 0

gen_a = make_gen(a, 16807, 4)
gen_b = make_gen(b, 48271, 8)

for _ in range(5_000_000):
    my_a = next(gen_a)
    my_b = next(gen_b)
    for _ in range(16):
        my_a, mod_a = divmod(my_a, 2)
        my_b, mod_b = divmod(my_b, 2)
        if mod_a != mod_b:
            break
    else:
        result += 1

print(result)
