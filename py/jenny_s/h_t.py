#!/usr/bin/python3
# This program picks a random person to pay the bills
# when many friends are seated in an outing.

import random

names = []
first_person = input("What is your name.? ")
names.append(first_person)

n = int(input("\nHow many other persons are on the table.? "))
for name in range(n):
    name = input("Enter the next person's name.. ")

    names.append(name)

print(names)
choice = random.choice(names)
print(f"\n{choice} will pay the bills this time.")

# OR, ALTERNATIVELY;
# names = input("Enter all the names seperated by comma.: ").split(",")
# choice = random.randint(0, len(names)-1)
# print(f"{names[choice]} will pay the bills this time!")
