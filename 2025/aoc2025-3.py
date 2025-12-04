import os

def argmax(values, start=0, end=0):
    if end == 0:
        end = None
    idx = None
    val = 0
    for i, x in enumerate(values[start:end], start):
        if x > val:
            idx = i
            val = x
    return idx


with open(os.path.join('data', 'aoc3.txt')) as file:
    nums = []
    for line in file:
        banks = list(map(int, line.rstrip()))
        first = argmax(banks, end=-1)
        second = argmax(banks, first+1)
        nums.append(banks[first] * 10 + banks[second])

    print(sum(nums))

with open(os.path.join('data', 'aoc3.txt')) as file:
    nums = []
    for line in file:
        banks = list(map(int, line.rstrip()))
        prod = 0
        idx = -1
        for i in range(12):
            idx = argmax(banks, max(i, idx + 1), i - 11)
            prod = 10 * prod + banks[idx]
        nums.append(prod)

    print(sum(nums))
