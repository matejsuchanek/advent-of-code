import os

def mark_board(board, n):
    for row in board:
        for i in range(5):
            if row[i] == n:
                row[i] = 'X'
                return True
    return False


def is_complete(board):
    for row in board:
        if all(c == 'X' for c in row):
            return True

    for i in range(5):
        if all(row[i] == 'X' for row in board):
            return True

    return False


boards = []
with open(os.path.join('data', 'aoc4.txt'), 'r') as file:
    first = next(file)
    numbers = [int(n) for n in first.split(',')]

    while next(file, None):
        board = []
        for i in range(5):
            line = next(file)
            board.append([int(n) for n in line.split()])
        boards.append(board)

done = set()
out = []
for n in numbers:
    for i, board in enumerate(boards):
        if i in done:
            continue
        if mark_board(board, n) and is_complete(board):
            done.add(i)
            unmarked = sum(sum(c for c in row if c != 'X') for row in board)
            out.append(unmarked * n)

print(out[0])
print(out[-1])
