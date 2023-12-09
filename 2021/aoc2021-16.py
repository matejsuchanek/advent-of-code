import os

hex_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

with open(os.path.join('data', 'aoc16.txt'), 'r') as file:
    line = next(file).rstrip()

binary = ''.join(hex_map[c] for c in line)

def parse(binary):
    out = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)
    if type_id == 4:
        index = 6
        value = 0
        last = False
        while not last:
            last = binary[index] == '0'
            add = int(binary[index+1:index+5], 2)
            value = 16 * value + add
            index += 5
        return (out, value, index)

    values = []
    length_type_id = binary[6]
    if length_type_id == '0':
        index = 22
        length = int(binary[7:22], 2)
        stop = length + index
        while index < stop:
            add, val, idx = parse(binary[index:])
            out += add
            values.append(val)
            index += idx

    elif length_type_id == '1':
        num = int(binary[7:18], 2)
        index = 18
        for i in range(num):
            add, val, idx = parse(binary[index:])
            out += add
            values.append(val)
            index += idx

    if type_id == 0:
        value = sum(values)
    elif type_id == 1:
        value = 1
        for val in values:
            value *= val
    elif type_id == 2:
        value = min(values)
    elif type_id == 3:
        value = max(values)
    elif type_id == 5:
        value = int(values[0] > values[1])
    elif type_id == 6:
        value = int(values[0] < values[1])
    elif type_id == 7:
        value = int(values[0] == values[1])

    return (out, value, index)

out, value, _ = parse(binary)
print(out)
print(value)
