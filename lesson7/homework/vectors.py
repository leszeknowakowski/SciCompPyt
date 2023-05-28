import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.z != other.z

    def __add__(self, other):
        addx = self.x + other.x
        addy = self.y + other.y
        addz = self.z + other.z
        return Vector(addx, addy, addz)

    def __sub__(self, other):
        subx = self.x - other.x
        suby = self.y - other.y
        subz = self.z - other.z
        return Vector(subx, suby, subz)

    def __mul__(self, other):
        dot = self.x * other.x + self.y * other.y + self.z * other.z
        return dot

    def cross(self, other):
        crossx = self.y * other.z - self.z * other.y
        crossy = self.z * other.x - self.x * other.z
        crossz = self.x * other.y - self.y * other.x
        return Vector(crossx, crossy, crossz)

    def length(self):
        leng = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return leng

    def __hash__(self):
        return hash((self.x, self.y, self.z))

