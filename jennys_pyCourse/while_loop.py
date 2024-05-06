#!/usr/bin/python3

n = 0
while True:
    a = int(input("Enter a number (0 to quit.): "))
    if a <= 0:
        break
    n += a
    print(n)

