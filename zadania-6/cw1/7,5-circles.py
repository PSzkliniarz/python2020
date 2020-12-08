from points import Point
from math import pi

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return f"Circle({self.pt.x},{self.pt.y},{self.radius})".format(self=self)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):          # pole powierzchni
        a = pi * self.radius * self.radius
        return round(a, 2)

    def move(self, x, y):      # przesuniecie o (x, y)
        return self.pt.x + x, self.pt.y + y

    def cover(self, other):    # najmniejszy okrąg pokrywający oba
        x = (self.pt.x + other.pt.x) / 2
        y = (self.pt.y + other.pt.y) / 2
        print("cover")

        return Circle(x, y, 2)


# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):

    circle1 = Circle(4, 4, 2)
    circle2 = Circle(4, 4, 2)

    def test_create(self):
        self.assertRaises(ValueError, Circle, 2, 3, -1)

    def test_repr(self):
        self.assertEqual(self.circle1.__repr__(), "Circle(4,4,2)", "Nie równe")

    def test_eq(self):
        self.assertTrue(self.circle1 == self.circle2)

    def test_ne(self):
        self.assertFalse(self.circle1 != self.circle2)

    def test_area(self):
        self.assertEqual(self.circle1.area(), 12.57)

    def test_move(self):
        self.assertEqual(self.circle1.move(2, 3), (6, 7))

   # def test_cover(self):
   #       # self.assertEqual(Circle.cover(Circle(2, 2, 1), Circle(3, 2, 1)), Circle(2.5,2.0,2))
   #      self.assertEqual(Circle(2, 2, 1).cover(Circle(3, 2, 2)),  Circle(2.5,2.0,2))



if __name__ == '__main__':
    unittest.main()


    print(Circle.cover(Circle(2, 2, 1), Circle(3, 2, 1)))