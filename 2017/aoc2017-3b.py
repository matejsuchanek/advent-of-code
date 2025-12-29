def iter_dirs():
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i or j:
                yield i, j


def value_for_position(data, pos):
    res = 0
    for i, j in iter_dirs():
        res += data.get((pos[0] + i, pos[1] + j), 0)
    return res


def run(num):
    steps = 1
    pos = (0, 0)
    dir_index = 0
    data = {}
    data[pos] = 1
    while True:
        for _ in range(2):
            my_dir = dirs[dir_index]
            for _ in range(steps):
                pos = pos[0] + my_dir[0], pos[1] + my_dir[1]
                value = value_for_position(data, pos)
                data[pos] = value
                if value > num:
                    return value

            dir_index = (dir_index + 1) % 4
        steps += 1


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
num = int(input())
print(run(num))
