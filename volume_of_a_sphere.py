#!/usr/bin/python3

from math import pi
from sys import argv


# Volume of a sphere calculation


R = argv[1]


def volume(R):
    return (4/3) * pi * (R ** 3)

volume(argv)
