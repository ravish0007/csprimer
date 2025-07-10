class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vec({self.x}, {self.y})'

    def __repr__(self):
        return f'Vec({self.x}, {self.y})'

    def __mul__(self, val):
        return Vec(self.x*val, self.y*val)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_magnitude(self):
        return (self.x**2 + self.y**2)**0.5
