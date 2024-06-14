#!/usr/bin/python3

from math import pi
from sys import argv


# Volume of a sphere calculation


R = argv[1]


def volume(R):
    '''
    Takes in the radius and returns the volume of a sphere.
    '''
    return (4/3) * pi * (R ** 3)

volume(argv)
