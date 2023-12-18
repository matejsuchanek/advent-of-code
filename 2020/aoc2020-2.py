import os

valid_count = valid_pos = 0
with open(os.path.join('data', 'aoc2.txt')) as f:
    for line in f:
        interval, letter, password = line.split()
        first, second = map(int, interval.split('-'))
        letter = letter[0]
        valid_count += first <= password.count(letter) <= second
        valid_pos += (password[first-1] == letter) != (password[second-1] == letter)

print(valid_count)
print(valid_pos)
