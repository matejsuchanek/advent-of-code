import os

numbers = []

with open(os.path.join('data', 'aoc9.txt')) as f:
    for line in f:
        num = int(line.rstrip())
        numbers.append(num)

invalid = None
for index in range(25, len(numbers)):
    num = numbers[index]
    last = numbers[index-25:index]
    ok = False
    for i, other in enumerate(last):
        diff = num - other
        if diff in [last[j] for j in range(25) if j != i]:
            ok = True
            break

    if not ok:
        invalid = num
        break
    numbers.append(num)

print(invalid)
for start, total in enumerate(numbers):
    for i in range(start+1, len(numbers)):
        total += numbers[i]
        if total >= invalid:
            break
    if total == invalid:
        rng = numbers[start:i+1]
        mn, mx = min(rng), max(rng)
        print(mn + mx)
        break
