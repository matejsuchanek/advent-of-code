import os

def run(poly):
    while True:
        new_poly = []
        for c in poly:
            new_poly.append(c)
            changed = True
            while changed:
                changed = False
                if len(new_poly) > 1:
                    a, b = new_poly[-2:]
                    if a != b and a.upper() == b.upper():
                        new_poly.pop()
                        new_poly.pop()
                        changed = True
        if len(poly) == len(new_poly):
            return len(poly)
        poly = new_poly


with open(os.path.join('data', 'aoc5.txt')) as file:
    string = next(file).strip()

poly = list(string)
least = run(poly)
print(least)

for c in set(map(str.upper, string)):
    poly = list(string.replace(c, '').replace(c.lower(), ''))
    aux = run(poly)
    if aux < least:
        least = aux

print(least)
