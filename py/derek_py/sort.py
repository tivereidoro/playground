#!/usr/bin/python3
import random

# Generate a random list
demo_list = []

# Populate the list with random numbers
for i in range(5):
    demo_list.append(random.randint
                     (1, 9))
    
print(f"\nUnsorted list: \n{demo_list}")
# print(demo_list.sort())  ... didn't work this way

# Lets sort with Bubble
a = len(demo_list) - 1
while a > 1:
    b = 0
    while b < a:
        # Check for highest
        if demo_list[b] > demo_list[b + 1]:   # Change '>' to '<' to reverse sort..
            # Switch the data
            temp_var = demo_list[b]
            demo_list[b] = demo_list[b + 1]
            demo_list[b + 1] = temp_var
        else: 
            pass

        b += 1
    a -= 1

print(f"\nSorted list: \n{demo_list}")

## For some reason, sorting a list with sort() is not working..
## Investigating this..
## DONE..!

# Another approach to using sort()
new_list = []

for i in range(5):
    new_list.append(random.randint(1, 9))
    
print('\nNew list')
print(new_list)

new_list.sort()
print(f"Sorted list with sort(): \n{new_list}")

"""
for _ in new_list:
    print(_, end=", ")
print()
"""