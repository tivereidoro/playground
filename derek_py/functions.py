#!/usr/bin/python3

import math


# Functions and their usage

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("\nKindly enter rectangle or circle!")

def rectangle_area():
    length = float(input("\nEnter the length : "))
    width = float(input("\nEnter the width : "))

    area = length * width

    print(f"\nThe area of the rectangle is {area}\n")


def circle_area():
    radius = float(input("\nEnter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    print("\nThe area of the circle is {:.2f}".format(area))


def main():
    print("\nHello there!  Welcome.")
    shape_type = input("\nWhat type of shape do you need its area.?")


    get_area(shape_type)


main()
