#!/usr/bin/python3

def islower(c):
    """
    Checks for capitalisation.
    Returns True if c is lowercase
    Returns False otherwise
    """
    if ord(c) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False
