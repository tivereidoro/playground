#!/usr/bin/python3
import math
# 1 paint_can = 7 sq.m of wall
# def  a func that takes height, width, and coverage
# output how many cans will be needed = (ht * wt)/7 sq.m then ceil() it.

wall_height = float(input("Enter the height of the wall in meters: "))
width = float(input("... width of wall in meters: "))
coverage = 7  # square meters


def cans(wall_height=1, width=1):
    number_of_cans = math.ceil(wall_height * width / coverage)
    return number_of_cans


print(f"You will need {cans(wall_height, width)} cans of paint.")
