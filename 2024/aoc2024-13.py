import os
from math import gcd

games = []

with open(os.path.join('data', 'aoc13.txt')) as file:
    while True:
        lines = [next(file), next(file)]
        prize = next(file)

        buttons = {}
        for char, line in zip('AB', map(str.rstrip, lines)):
            X, Y = line.removeprefix(f'Button {char}: ').split(', ')
            buttons[char] = (
                int(X.removeprefix('X+')),
                int(Y.removeprefix('Y+'))
            )

        X, Y = prize.rstrip().removeprefix('Prize: ').split(', ')
        X = int(X.removeprefix('X='))
        Y = int(Y.removeprefix('Y='))

        games.append((buttons, (X, Y)))

        if next(file, None) is None:
            break

for add in (0, 10_000_000_000_000):
    result = 0
    for buttons, (X, Y) in games:
        X += add
        Y += add

        div = gcd(*buttons['A'])

        nom = (buttons['A'][1] // div) * X - (buttons['A'][0] // div) * Y
        denom = (buttons['A'][1] // div) * buttons['B'][0] \
                - (buttons['A'][0] // div) * buttons['B'][1]

        B, mod = divmod(nom, denom)
        if mod != 0:
            continue

        A, check = divmod(X - buttons['B'][0] * B, buttons['A'][0])
        if check == 0 and A >= 0 and B >= 0:
            result += 3 * A + B

    print(result)
