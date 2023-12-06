import math
import os

with open(os.path.join('data', 'aoc6.txt'), 'r') as file:
    times = [int(x) for x in next(file).split() if x.isdigit()]
    dist = [int(x) for x in next(file).split() if x.isdigit()]

n = []

# s < vt
# s < h(t-h) = ht - h^2
# d < ht - h^2
# h^2 - ht + d < 0
# h_1 < 0.5 * (t - sqrt(t^2 - 4d))
# h_2 > 0.5 * (t + sqrt(t^2 - 4d))

for t, d in zip(times, dist):
    h_1 = 0.5 * (t - math.sqrt(t*t - 4*d))
    h_2 = 0.5 * (t + math.sqrt(t*t - 4*d))

    n.append(1 + math.ceil(h_2 - 1) - math.floor(h_1 + 1))

print(math.prod(n))

t = int(''.join(map(str, times)))
d = int(''.join(map(str, dist)))

h_1 = 0.5 * (t - math.sqrt(t*t - 4*d))
h_2 = 0.5 * (t + math.sqrt(t*t - 4*d))

print(1 + math.ceil(h_2 - 1) - math.floor(h_1 + 1))
