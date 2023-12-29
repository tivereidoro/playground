# Modules practice


def fib(n):
    a = 0
    b = 1

    while a < n:
        print(a, end=' ')
        a = b
        b = a+b
    print()

# Make this file usable as a script as well as an importable module.


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
