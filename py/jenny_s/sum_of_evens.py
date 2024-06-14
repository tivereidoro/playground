#!/usr/bin/python3
''' Program to calculate the sum of the even numbers btw 1 to 100
    1 and 100 inclusive.'''

even_total = 0
for i in range(2, 101, 2):
    even_total += i
print(f"The sum of the even numbers is {even_total}")
