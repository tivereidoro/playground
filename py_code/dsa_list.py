#!/usr/bin/python3

def replace_in_list(my_list, idx, element=0):
    my_list[idx] = element
    return my_list

list_demo = [3, 75, 2, 8, 95]
print(replace_in_list(list_demo, 3))
