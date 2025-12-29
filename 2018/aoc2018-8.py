import os


def process_simple(index):
    children = nums[index]
    entries = nums[index+1]
    total = 0
    index += 2
    for i in range(children):
        index, out = process_simple(index)
        total += out
    total += sum(nums[index:index+entries])
    return index + entries, total


def process_complex(index):
    children = nums[index]
    entries = nums[index+1]
    value = 0
    index += 2
    if children:
        values = [0]
        for i in range(children):
            index, sub = process_complex(index)
            values.append(sub)
        count = len(values) - 1
        for e in nums[index:index+entries]:
            if e <= count:
                value += values[e]
    else:
        value = sum(nums[index:index+entries])

    return index + entries, value


with open(os.path.join('data', 'aoc8.txt')) as file:
    nums = [int(x) for x in next(file).split()]

_, total = process_simple(0)
print(total)

_, total = process_complex(0)
print(total)
