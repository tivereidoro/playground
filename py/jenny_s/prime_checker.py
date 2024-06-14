#!/usr/bin/python3
from math import ceil

def is_prime(number):
    prime = True
    if number == 1:
        prime = False
    for i in range(2, ceil(number/2)+1):
        if number % i == 0:
            prime = False
    if prime:
        print(f"\n{number} is a prime number.")
    else:
        print(f"\n{number} is NOT a prime number.!")


num = int(input("Enter a number to check: "))
is_prime(num)
