# Exercise: From the demo list given, create a list containing [8, 6, 4, 2] in this exact order.
demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#One approach is to slice, then reverse the llist with the reversed() function.
new_list = demo_list[1:8:2]
print(list(reversed(new_list)))

#However, even better, this will render the reverse approach above unnecessary.
print(demo_list[7::-2])
