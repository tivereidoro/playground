#!/usr/bin/python3


# create a list of primes

#take the number length of prime
prime_length = int(input('Enter the max prime number you want : '))

prime_list = []

for i in range(2, prime_length):
    if (i % 2) != 0:
        prime_list.append(i)
    else:
        continue

print(prime_list)
