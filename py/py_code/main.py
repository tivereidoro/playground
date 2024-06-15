#!/usr/bin/python3

class Customer:
    """ My demo class for practicing
    OOP with python.
    """

    def __init__(self, name, membership_type) -> None:
        """ Initialisation method.
        """
        self.name = name
        self.membership_type = membership_type

    def __str__(self) -> str:
        """ Stringify member instance.
        """
        return f"Customer: {self.name}\nSubscription: {self.membership_type} member."
    
    def 

