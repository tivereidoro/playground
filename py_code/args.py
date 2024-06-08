#!/usr/bin/python3
from sys import argv


def args():
    """List and number of arguments
    Args:
        None.

    Returns:
        Nothing
    """

    if len(argv) == 1:
        print(f"0 arguments.")
    elif len(argv) == 2:
        print(f"{len(argv)-1} argument:\n1: {argv[1]}")
    else:
        print(f"{len(argv)-1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")



if __name__ == "__main__":
    args()
