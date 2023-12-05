import os

words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

prim = sec = 0

with open(os.path.join('data', 'aoc1.txt'), 'r') as file:
    for line in file:
        digits = []
        all_digits = []
        for i in range(len(line)):
            x = line[i]
            if x.isdigit():
                digits.append(int(x))
                all_digits.append(int(x))
            else:
                for word in words:
                    if line[i:i+len(word)] == word:
                        all_digits.append(words[word])
                        break

        prim += digits[0] * 10 + digits[-1]
        sec += all_digits[0] * 10 + all_digits[-1]

print(prim)
print(sec)
