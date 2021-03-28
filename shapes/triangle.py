#!/usr/bin/env python

"""
Author: Krzysztof Achinger
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains a height value, base value
    a_side value and c_side value.
    """

    def __init__(self, height, base, a_side, c_side):
        self.height = height
        self.base = base
        self.a_side = a_side
        self.c_side = c_side

    def area(self):
        """
        Compute the area using the formula height * base / 2
        """
        area = self.height * self.base / 2
        return round(area, 2)

    def perimeter(self):
        """
        Compute the perimeter using the formula (a_side + base + c_side)
        """
        return self.a_side + self.base + self.c_side

    def is_equilateral(self):
        """
        Determine if the triangle is a eqilateral by comparing all three sides
        for equality.
        """
        return self.a_side == self.base == self.c_side

    def is_isosceles(self):
        """
        Determine if the triangle is isosceles by checking if two but not 3 sides
        are equal.
        """
        return len(set([self.a_side, self.base, self.c_side])) == 2
