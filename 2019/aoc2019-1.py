import os

with open(os.path.join('data', 'aoc1.txt')) as file:
    lines = file.read().splitlines()

fuel = lambda x: int(x) // 3 - 2
print(sum(map(fuel, lines)))

more = lambda x: max(x, 0) + (total_fuel(x) if x > 0 else 0)
total_fuel = lambda x: more(fuel(x))
print(sum(map(total_fuel, lines)))
