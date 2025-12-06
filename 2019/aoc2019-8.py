import os

with open(os.path.join('data', 'aoc8.txt')) as file:
    data = file.read().strip()

x, y = 25, 6
px_per_layer = x * y

best = px_per_layer + 1
start, end = 0, px_per_layer
while start < len(data):
    zeros = data.count('0', start, end)
    if zeros < best:
        best = zeros
        out = data.count('1', start, end) * data.count('2', start, end)
    start = end
    end += px_per_layer

print(out)

image = [None] * px_per_layer
for i in range(px_per_layer):
    pos = i
    px = data[pos]
    while px == '2':
        pos += px_per_layer
        px = data[pos]
    image[i] = px

start = 0
while start < px_per_layer:
    print(''.join('#' if c == '1' else ' ' for c in image[start:start + x]))
    start += x
