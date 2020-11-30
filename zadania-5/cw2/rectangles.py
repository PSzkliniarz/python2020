from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[{self.pt1},{self.pt2}]".format(self=self)

    def __repr__(self):   # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({self.pt1.x},{self.pt1.y},{self.pt2.x},{self.pt2.y})".format(self=self)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):   # zwraca środek prostokąta
        x = int((self.pt1.x + self.pt2.x) / 2)
        y = int((self.pt1.y + self.pt2.y) / 2)
        return x, y

    def area(self):   # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y): pass  # przesunięcie o (x, y)


# Kod testujący moduł.

import unittest


class TestRectangle(unittest.TestCase):

    def test_print(self):
        self.assertEqual(Rectangle.__str__(Rectangle(1, 1, 2, 2)), "[(1,1),(2,2)]")
        self.assertEqual(Rectangle.__repr__(Rectangle(1, 1, 2, 2)), "Rectangle(1,1,2,2)")

    def test_cmp(self):
        self.assertTrue(Rectangle.__eq__(Rectangle(1, 1, 2, 2), Rectangle(1, 1, 2, 2)), "Powinny się pokrywać")
        self.assertTrue(Rectangle.__ne__(Rectangle(1, 1, 2, 2), Rectangle(1, 1, 3, 3)), "Powinny się różnić")

    def test_center(self):
        self.assertEqual(Rectangle.center(Rectangle(1, 1, 3, 3)), (2, 2))

    def test_area(self):
        self.assertTrue(Rectangle.area(Rectangle(1, 1, 3, 3)), 4)

r1 = Rectangle(1, 1, 2, 2)
r2 = Rectangle(1, 1, 2, 2)
print(r1)
print(r1.pt1.x)

print(Rectangle.__ne__(r1, r2))
