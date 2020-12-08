from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if not x1 < x2 or not y1 < y2:
            raise ValueError("Błędne wartośći")

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
        return Point(x, y)

    def area(self):   # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        x1 = self.pt1.x + x
        x2 = self.pt2.x + x
        y1 = self.pt1.y + y
        y2 = self.pt2.y + y
        return Rectangle(x1, y1, x2, y2)

    def intersection(self, other):  # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):     # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)


    def make4(self):            # zwraca krotkę czterech mniejszych
        big_center = self.center()


        rectangle1 = Rectangle(self.pt1.x, self.pt1.y, big_center.x, big_center.y)
        rectangle2 = Rectangle(self.pt1.x, big_center.y, big_center.x, self.pt2.y)
        rectangle3 = Rectangle(big_center.x, self.pt1.y, self.pt2.x, big_center.y)
        rectangle4 = Rectangle(big_center.x, big_center.y, self.pt2.x, self.pt2.y)

        return [rectangle1, rectangle2, rectangle3, rectangle4]

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    rectangle1 = Rectangle(1, 1, 2, 2)
    rectangle2 = Rectangle(1, 1, 3, 3)
    rectangle3 = Rectangle(1, 1, 5, 5)

    def test_create(self):
        self.assertRaises(ValueError, Rectangle, 5, 5, 2, 3)


    def test_str(self):
        self.assertEqual(Rectangle.__str__(Rectangle(1, 1, 2, 2)), "[(1,1),(2,2)]")

    def test_rept(self):
        self.assertEqual(Rectangle.__repr__(Rectangle(1, 1, 2, 2)), "Rectangle(1,1,2,2)")

    def test_cmp(self):
        self.assertTrue(Rectangle.__eq__(Rectangle(1, 1, 2, 2), Rectangle(1, 1, 2, 2)), "Powinny się pokrywać")

    def test_ne(self):
        self.assertTrue(Rectangle.__ne__(Rectangle(1, 1, 2, 2), Rectangle(1, 1, 3, 3)), "Powinny się różnić")

    def test_center(self):
        self.assertEqual(Rectangle.center(Rectangle(1, 1, 3, 3)), Point(2, 2))

    def test_area(self):
        self.assertTrue(Rectangle.area(Rectangle(1, 1, 3, 3)), 4)

    def test_move(self):
        self.assertTrue(self.rectangle1.move(3, 4), Rectangle(4, 4, 6, 6))

    def test_intersiction(self):
        self.assertEqual(self.rectangle1.intersection(Rectangle(1, 1, 3, 3)), Rectangle(1, 1, 2, 2))

    def test_cover(self):
        self.assertEqual(self.rectangle1.cover(Rectangle(1, 1, 3, 3)), Rectangle(1, 1, 3, 3))

    def test_make4(self):
        self.assertEqual(Rectangle(1, 1, 5, 5).make4(), [Rectangle(1, 1, 3, 3), Rectangle(1, 3, 3, 5),
                                                         Rectangle(3, 1, 5, 3), Rectangle(3, 3, 5, 5)])



if __name__=='__main__':
    unittest.main()