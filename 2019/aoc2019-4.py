data = input()

start, stop = data.split('-')
cur  = list(map(int, start))
stop = list(map(int, stop))
out1 = out2 = 0
r_a, r_b = range(5), range(1, 6)

while cur != stop:
    at_least_two = just_two = False
    counter = 1
    for i, j in zip(r_a, r_b):
        x, y = cur[i], cur[j]
        if x > y:
            at_least_two = just_two = False
            counter = 1  # whatever except two
            break
        if x == y:
            at_least_two = True
            counter += 1
        else:
            if counter == 2:
                just_two = True
            counter = 1

    out1 += at_least_two
    out2 += (just_two or counter == 2)

    i = 5
    cur[i] += 1
    while i:
        if cur[i] == 10:
            cur[i] = 0
            i -= 1
            cur[i] += 1
        else:
            break

print(out1)
print(out2)
