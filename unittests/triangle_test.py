"""
Author: Krzysztof Achinger
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.isosceles_triangle = Triangle(5, 5, 5, 7.07)
        self.equilateral_triangle = Triangle(6.93, 8, 8, 8)
        self.triangle = Triangle(24, 50, 30, 40)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.isosceles_triangle.area(), 12.5)
        self.assertEqual(self.equilateral_triangle.area(), 27.72)
        self.assertEqual(self.triangle.area(), 600)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.isosceles_triangle.perimeter(), 17.07)
        self.assertEqual(self.equilateral_triangle.perimeter(), 24)
        self.assertEqual(self.triangle.perimeter(), 120)

    def test_is_equilateral(self):
        """
        Confirm or deny if the triangle is a equilateral.
        """
        self.assertFalse(self.isosceles_triangle.is_equilateral())
        self.assertTrue(self.equilateral_triangle.is_equilateral())
        self.assertFalse(self.triangle.is_equilateral())

    def test_is_isosceles(self):
        """
        Confirm or deny if the triangle is a equilateral.
        """
        self.assertTrue(self.isosceles_triangle.is_isosceles())
        self.assertFalse(self.equilateral_triangle.is_isosceles())
        self.assertFalse(self.triangle.is_isosceles())
