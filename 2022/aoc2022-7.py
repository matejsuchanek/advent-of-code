import os

class Directory:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files = {}

    def get_size(self):
        out = sum(self.files.values())
        out += sum(d.get_size() for d in self.dirs.values())
        return out

    def add_empty_dir(self, name):
        self.dirs[name] = Directory(name, self)

    def iter_subdirs(self):
        for d in self.dirs.values():
            yield d
            yield from d.iter_subdirs()


root = Directory('/')
path = root

with open(os.path.join('data', 'aoc7.txt'), 'r') as file:
    listing = False
    for line in map(str.split, file):
        if line[0] == '$':
            listing = False
            if line[1] == 'cd':
                if line[2] == '/':
                    path = root
                elif line[2] == '..':
                    path = path.parent
                    assert path is not None
                else:
                    path = path.dirs[line[2]]
            elif line[1] == 'ls':
                listing = True
        else:
            assert listing
            if line[0] == 'dir':
                path.add_empty_dir(line[1])
            else:
                assert line[0].isdigit()
                path.files[line[1]] = int(line[0])

total = 0
for d in root.iter_subdirs():
    size = d.get_size()
    if size <= 100_000:
        total += size
print(total)

unused = 70_000_000 - root.get_size()
best = float('inf')
for d in root.iter_subdirs():
    size = d.get_size()
    if unused + size >= 30_000_000:
        best = min(size, best)
print(best)
