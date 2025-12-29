from knot_hash import knot_hash

string = input()

out = 0
for i in range(128):
    h = knot_hash(f'{string}-{i}')
    out += ''.join(map(lambda c: bin(int(c, 16))[2:], h)).count('1')

print(out)
