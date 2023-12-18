import os

nums = []
diffs = set()
with open(os.path.join('data', 'aoc1.txt')) as f:
    for line in f:
        num = int(line.rstrip())
        nums.append(num)
        diffs.add(2020 - num)

for num in nums:
    if num in diffs:
        print(num * (2020 - num))
        break

stop = False
for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            s = num1 + num2 + num3
            if s == 2020:
                print(num1 * num2 * num3)
                stop = True
                break
        if stop:
            break
    if stop:
        break
