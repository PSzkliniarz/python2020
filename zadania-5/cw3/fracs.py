from math import gcd, floor,fmod

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{self.x}".format(self=self)
        else:
            return "{self.x}/{self.y}".format(self=self)

    def __repr__(self):         # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return self.x * other.y == self.y * other.x

    def __ne__(self, other):
        return self.x * other.y != self.y * other.x

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self.x * other.y <= self.y * other.x

    def __gt__(self, other):
        return self.x * other.y > self.y * other.x

    def __ge__(self, other):
        return self.x * other.y >= self.y * other.x

    def __add__(self, other):   # frac1 + frac2
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y
        return Frac(x, y)

    def __sub__(self, other):   # frac1 - frac2
        x = self.x * other.y - self.y * other.x
        y = self.y * other.y
        nwd = gcd(x, y)
        return Frac(x/ nwd, y/ nwd)

    def __mul__(self, other):   # frac1 * frac2
        x = self.x * other.x
        y = self.y * other.y
        nwd = gcd(x, y)
        return Frac(x / nwd, y / nwd)

    #def __div__(self, other): pass  # frac1 / frac2, Python 2

    def __truediv__(self, other):   # frac1 / frac2, Python 3
        x = self.x * other.y
        y = self.y * other.x
        nwd = gcd(x, y)
        return Frac(x / nwd, y / nwd)

    def __floordiv__(self, other):   # frac1 // frac2, opcjonalnie
        x = self.x * other.y
        y = self.y * other.x
        return floor(x / y)

    def __mod__(self, other):   # frac1 % frac2, opcjonalnie
        x = self.x * other.y
        y = self.y * other.x
        nwd = gcd(x, y)
        return fmod(x / nwd, y / nwd)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return float(self.x / self.y)

    def __hash__(self):
        return hash(float(self))  # immutable fracs

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):

    f1 = Frac(1, 2)
    f2 = Frac(3, 4)


    def test_print(self):
        self.assertEqual(self.f1.__str__(), "1/2")
        self.assertEqual(self.f1.__repr__(), "Frac(1, 2)")

    def test_cmp(self):
        self.assertTrue(self.f1.__eq__(self.f1))
        self.assertFalse(self.f1 == self.f2)

        self.assertTrue(self.f1 != self.f2, "ne")
        self.assertFalse(self.f1 != self.f1, "ne")

        self.assertTrue(self.f1 < self.f2, "lt")
        self.assertFalse(self.f1 < self.f1, "lt")

        self.assertTrue(self.f1 <= self.f1, "le")
        self.assertFalse(self.f2 <= self.f1, "le")

        self.assertTrue(self.f2 > self.f1, "gt")
        self.assertFalse(self.f2 > self.f2, "gt")

        self.assertTrue(self.f2 >= self.f2, "ge")
        self.assertFalse(self.f1 >= self.f2, "ge")

    def test_math(self):
        self.assertEqual(self.f1 + self.f2, Frac(5, 4))
        self.assertEqual(self.f2 - self.f1, Frac(1, 4))
        self.assertEqual(self.f1 * self.f2, Frac(3, 8))
        self.assertEqual(self.f1 / self.f2, Frac(2, 3))
        self.assertEqual(self.f2 // self.f2, 1)

    def test_mod(self):
        self.assertAlmostEqual(self.f2 % self.f1, float(1), msg="mod")

    def test_neg(self):
        self.assertEqual(-self.f1, Frac(-self.f1.x, self.f1.y))

    def test_invert(self):
        self.assertEqual(~self.f1, Frac(self.f1.y, self.f1.x))

    def test_float(self):
        self.assertEqual(float(self.f1), float(self.f1.x / self.f1.y))



if __name__ == '__main__':
    unittest.main()