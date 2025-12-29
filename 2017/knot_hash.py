def knot_hash(string):
    lengths = list(map(ord, string))
    lengths.extend([17, 31, 73, 47, 23])

    l = list(range(256))
    pos = 0
    skip = 0

    for x in range(64):
        for length in lengths:
            if length > len(l):
                continue
            end = (pos + length - 1) % len(l)
            if length > 1:
                stack = []
                while True:
                    stack.append(l[end])
                    if pos == end:
                        break
                    if end == 0:
                        end = len(l)
                    end -= 1
                for i, val in enumerate(stack, pos):
                    l[i % len(l)] = val
            pos = (pos + length + skip) % len(l)
            skip += 1

    out = ''

    for start in range(0, 256, 16):
        dense = l[start]
        for i in range(1, 16):
            dense ^= l[start + i]
        out += '%02x' % dense

    return out
