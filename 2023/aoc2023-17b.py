import heapq
import os

grid = []

with open(os.path.join('data', 'aoc17.txt'), 'r') as file:
    for line in file:
        row = []
        row.extend(map(int, line.rstrip()))
        grid.append(row)

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

turns = {
    NORTH: [NORTH, EAST, WEST],
    SOUTH: [SOUTH, EAST, WEST],
    WEST: [WEST, SOUTH, NORTH],
    EAST: [EAST, SOUTH, NORTH],
}

end = (len(grid) - 1, len(grid[-1]) - 1)
h = lambda coord: (end[0] - coord[0]) + (end[1] - coord[1])

heap = []
heapq.heappush(
    heap,
    (
        grid[1][0] + h((1, 0)),
        (grid[1][0], (1, 0), SOUTH, 1)
    )
)
heapq.heappush(
    heap,
    (
        grid[0][1] + h((0, 1)),
        (grid[0][1], (0, 1), EAST, 1)
    )
)

seen = set()

while heap:
    _, entry = heapq.heappop(heap)
    loss, pos, direct, count = entry
    if (pos, direct, count) in seen:
        continue

    seen.add((pos, direct, count))
    if pos == end and count >= 4:
        print(loss)
        break

    for turn in turns[direct]:
        if turn != direct and count < 4:
            continue
        if turn == direct and count == 10:
            continue

        if turn == direct:
            new_count = count + 1
        else:
            new_count = 1

        new_x = pos[0] + turn[0]
        new_y = pos[1] + turn[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[new_x]):
            new = (new_x, new_y)
            new_loss = loss + grid[new_x][new_y]
            new_entry = (new_loss, new, turn, new_count)
            heapq.heappush(
                heap,
                (new_loss + h(new), new_entry)
            )
