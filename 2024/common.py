class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def _cast(cls, other):
        if isinstance(other, int):
            return cls(other, other)
        if isinstance(other, tuple):
            return cls(*other)
        return other

    def __add__(self, other):
        other = self._cast(other)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        other = self._cast(other)
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return Vector(self.x * factor, self.y * factor)

    __rmul__ = __mul__

    def __floordiv__(self, div):
        return Vector(self.x // div, self.y // div)

    def __mod__(self, other):
        other = self._cast(other)
        return Vector(self.x % other.x, self.y % other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __hash__(self):
        return hash((self.x, self.y))


looks = [
    Vector(-1, 0),
    Vector(0, +1),
    Vector(+1, 0),
    Vector(0, -1),
]
looks_diag = [
    Vector(-1, 0),
    Vector(-1, 1),
    Vector(0, 1),
    Vector(1, 1),
    Vector(1, 0),
    Vector(1, -1),
    Vector(0, -1),
    Vector(-1, -1),
]
