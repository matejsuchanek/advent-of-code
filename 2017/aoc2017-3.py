def run(num):
    pos = (0, 0)
    i = 1
    steps = 1
    dir_index = 0
    while True:
        for _ in range(2):
            my_dir = dirs[dir_index]
            for _ in range(steps):
                i += 1
                pos = pos[0] + my_dir[0], pos[1] + my_dir[1]
                if num == i:
                    return pos
            dir_index = (dir_index + 1) % 4
        steps += 1


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
num = int(input())

pos = run(num)
print(sum(map(abs, pos)))
