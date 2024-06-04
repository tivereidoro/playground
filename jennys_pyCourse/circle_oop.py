#!/usr/bin/python3
from math import pi, pow


class Circle:
    """
    This class is for all circle ish.."""
    def __init__(self, rad) -> None:
        self.radius = rad
        self.diameter = rad * 2

    def circumference(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * pow(self.radius, 2)


ring = Circle(3)
print(ring.area())
print(f"The circumference is {ring.circumference()}")
