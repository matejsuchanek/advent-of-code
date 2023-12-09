import os


def dice_gen():
    while True:
        yield from range(1, 101)


start = []
with open(os.path.join('data', 'aoc21.txt'), 'r') as file:
    for _ in range(2):
        line = next(file)
        *_, n = line.rstrip().rpartition(': ')
        start.append(int(n))


position = start[:]
score = [0, 0]
dice = dice_gen()
stop = False
times = 0
while not stop:
    for i, pos in enumerate(position):
        move = 0
        for _ in range(3):
            move += next(dice)
        times += 3
        pos = (pos + move) % 10
        if pos == 0:
            pos = 10
        position[i] = pos
        score[i] += pos
        if score[i] >= 1000:
            stop = True
            break

out = times * min(score)
print(out)


def dfs(position, score, i):
    ret = [0, 0]
    for move, times in mapping.items():
        pos = (position[i] + move) % 10
        if pos == 0:
            pos = 10
        sc = score[i] + pos
        if sc >= 21:
            ret[i] += times
        else:
            if i == 0:
                out = dfs((pos, position[1]), (sc, score[1]), 1)
            elif i == 1:
                out = dfs((position[0], pos), (score[0], sc), 0)
            ret[0] += times * out[0]
            ret[1] += times * out[1]

    return ret


mapping = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

score = (0, 0)
finite = dfs(start, score, 0)
print(max(finite))
