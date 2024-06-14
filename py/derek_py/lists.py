#!/usr/bin/python3
# This code expands the details
# of the process of a Bubble Sort.

import random
import math

# Generate a random list of random values btw 1 and 9.
random_list = []
for i in range(5):
    random_list.append(random.randint(1, 10))

print(random_list)

# Start the Bubble Sort:
# which checks and sorts from the largest num at the end of list,
# to the least num at the beginning of the list.

m = len(random_list) - 1

while m > 1:
    n = 0
    while n < m:
        print(f"\nIs {random_list[n]} > {random_list[n+1]}")

        if random_list[n] > random_list[n + 1]:
            print("Switch !")

            # Swap the numbers
            temp = random_list[n]
            random_list[n] = random_list[n + 1]
            random_list[n + 1] = temp
        else:
            print("Don't Switch")

        n += 1

        for k in random_list:
            print(k, end=", ")
        print()

    # So at the end of the 1st round, the largest num in that round goes to the last index
    print("END OF ROUND")

    m -= 1

# for k in random_list:
#     print(k, end=", ")
# print()

print(f"\nThe final Bubble Sorted list is: \n{random_list}")