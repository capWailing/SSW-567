"""
    author: Zituo Yan
    description: Test of HW 01
    date: 29/01/2020
"""
import math
import unittest
from HW_01_Zituo_Yan import classify_triangle


class TestClassifyTriangle(unittest.TestCase):
    def test_classify_triangle(self):
        """
            test classify triangle
        """
        self.assertEqual(classify_triangle("a", 2, "c"), "invalid input")
        self.assertEqual(classify_triangle(1, 2, 3), "not a triangle!")
        self.assertEqual(classify_triangle(3, 4, 5), "right triangle!")
        self.assertEqual(classify_triangle(3, 3, 3), "equilateral triangle!")
        self.assertEqual(classify_triangle(3, 3, 5), "isosceles triangle!")
        self.assertEqual(classify_triangle(2, 3, 4), "scalene triangle!")
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "isosceles right triangle!")


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)