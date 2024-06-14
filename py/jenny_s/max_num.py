#!/usr/bin/python3
'''Program to determine the maximum numbere in a list.'''

num_list = input("Enter the numbers seperated with a space: ").split()
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
print(num_list)
print(max(num_list))

max_num = 0
for num in num_list:
    if num > max_num:
        max_num = num
else:
    print(f"\nThe max number is {max_num}.")

# 23 45 8 54 90
