#!/usr/bin/python3

class A:
    pass

class B:
    pass

class C:
    pass

class D:
    pass

class E:
    pass

class F(A, B, C):
    pass

class G(D, B, E):
    pass

class H(D, A):
    pass

class Z(F, G, H):
    pass

print(Z.__mro__)