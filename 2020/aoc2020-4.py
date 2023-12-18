import os

passports = []
current = []
fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}

with open(os.path.join('data', 'aoc4.txt')) as f:
    for line in f:
        line = line.rstrip()
        if not line:
            passports.append(' '.join(current))
            current[:] = []
        else:
            current.append(line)
    if current:
        passports.append(' '.join(current))

bounds = {
    'byr': (1920, 2002),
    'iyr': (2010, 2020),
    'eyr': (2020, 2030)
}
eyes = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
hexdec = set('0123456789abcdef')

valid = present = 0
for pp in passports:
    data = {}
    for entry in pp.split():
        key, _, value = entry.partition(':')
        data[key] = value
    is_valid = (fields <= data.keys())

    is_present = False
    if is_valid:
        for key, value in data.items():
            is_present = False
            if key in bounds:
                if len(value) == 4 and value.isdigit():
                    int_value = int(value)
                    lower, upper = bounds[key]
                    is_present = lower <= int_value <= upper
            elif key == 'hgt':
                if value.endswith(('cm', 'in')):
                    if value[:-2].isdigit():
                        height, unit = int(value[:-2]), value[-2:]
                        if unit == 'cm':
                            is_present = 150 <= height <= 193
                        elif unit == 'in':
                            is_present = 59 <= height <= 76
            elif key == 'hcl':
                if len(value) == 7 and value[0] == '#':
                    is_present = set(value[1:]) <= hexdec
            elif key == 'ecl':
                is_present = value in eyes
            elif key == 'pid':
                if len(value) == 9:
                    is_present = value.isdigit()
            elif key == 'cid':
                is_present = True

            if not is_present:
                break

    valid += is_valid
    present += is_present

print(valid)
print(present)
