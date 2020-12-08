import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "({self.x},{self.y})".format(self=self)

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point({self.x},{self.y})".format(self=self)

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):  # v1 - v2
        return self.x - other.x, self.y - other.y

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x, self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

import unittest


class TestPoint(unittest.TestCase):
    def test_print(self):
        self.assertEqual(Point.__str__(Point(2, 3)), "(2,3)")
        self.assertEqual(Point.__repr__(Point(2, 3)), "Point(2,3)")

    def test_cmp(self):
        self.assertTrue(Point.__eq__(Point(2, 2),Point(2, 2)))
        self.assertFalse(Point.__ne__(Point(2, 2),Point(2, 2)))

    def test_math(self):
        self.assertEqual(Point.__add__(Point(2, 3),Point(4, 5)), (6, 8))
        self.assertEqual(Point.__sub__(Point(2, 3),Point(4, 5)), (-2, -2))
        self.assertEqual(Point.__mul__(Point(2, 3),Point(4, 5)), (8, 15))
        self.assertEqual(Point.cross(Point(2, 3),Point(4, 5)),  -2)

    def test_leght(self):
        self.assertEqual(Point(3, 4).length(), 5, "Should be 5")

    def tes_hash(self):
        self.assertEqual(Point.__hash__(Point(3, 4)), 1690007738)


    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


# p1 = Point(3, 4)
# p2 = Point(2, 5)
# print(p1)
# print(p1.__repr__())
# print(Point.__eq__(p1, p2))
# print(Point.__ne__(p1, p2))
#
# print(Point.__add__(p1, p2))
#
# print(p1.length())
if __name__ == "__main__":
    p1 = Point(3,4)
    print(p1)
    print(p1.__hash__())
    unittest.main()
