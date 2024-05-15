#!/usr/bin/python3

def info_person(**kwags):
    # for key, value in kwags.items():
    #     print(key, value)
    print(kwags)


def multiplying(*numbers):
    c = 1
    for i in numbers:
        c *= i
    return c


print(multiplying(3, 2, 6, 8))

info_person(name='Tivere', age=20, address='BDPA')
