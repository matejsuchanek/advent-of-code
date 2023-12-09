from math import ceil, sqrt
import os

with open(os.path.join('data', 'aoc17.txt'), 'r') as file:
    line = next(file)
    target_area, _, right = line.partition(': ')
    x_data, y_data = right.split(', ')
    x1, x2 = map(int, x_data[2:].split('..'))
    y1, y2 = map(int, y_data[2:].split('..'))

best = 0
min_x_vel = ceil((sqrt(1 + 8 * x1) - 1) * .5)

total = 0
for x_vel_ in range(min_x_vel, x2 + 1):
    init = y1
    while True:
        x_vel, y_vel = x_vel_, init
        y = 0
        if init >= 0:
            top = (y_vel * (y_vel + 1)) // 2

            aux = max(1, x_vel - 2*y_vel)
            n = x_vel - aux + 1
            x = ((aux + x_vel) * n) // 2

            x_vel -= n
            y_vel = -(init + 1)
            if x > x2 or y_vel < y1:
                break
        else:
            top = 0
            x = 0

        while y >= y1 and x <= x2:
            x += x_vel
            y += y_vel

            if x1 <= x <= x2 and y1 <= y <= y2:
                best = max(top, best)
                total += 1
                break

            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
            y_vel -= 1

        init += 1

print(best)
print(total)
