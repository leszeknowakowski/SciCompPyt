import unittest
from vectors import Vector
class TestVector(unittest.TestCase):
    def test_equality(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(1, 2, 3)
        self.assertEqual(v1, v2)

    def test_inequality(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        self.assertNotEqual(v1, v2)

    def test_addition(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        result = v1 + v2
        self.assertEqual(result, Vector(5, 7, 9))

    def test_subtraction(self):
        v1 = Vector(4, 5, 6)
        v2 = Vector(1, 2, 3)
        result = v1 - v2
        self.assertEqual(result, Vector(3, 3, 3))

    def test_dot_product(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        result = v1 * v2
        self.assertEqual(result, 32)

    def test_cross(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        result = v1.cross(v2)
        self.assertEqual(result, Vector(-3, 6, -3))

    def test_length(self):
        v = Vector(3, 4, 5)
        result = v.length()
        self.assertAlmostEqual(result, 7.07106781187, places=6)

    def test_invalid_vector_creation(self):
        with self.assertRaises(ValueError):
            v = Vector(1, 2)
        with self.assertRaises(ValueError):
            v = Vector(1)
        with self.assertRaises(ValueError):
            v = Vector()

if __name__ == '__main__':
    unittest.main()