#!/usr/bin/python3
'''Program to calculate average height from a list of heights.'''

heights = input("Enter the heights, each seperated by a comma.: ").split(",")
print(heights)
sum = 0
for height in heights:
    sum += int(height)
else:
    print('Done.!!')

average = sum/len(heights)
print(f"\nThe average height is {average}cm.")
