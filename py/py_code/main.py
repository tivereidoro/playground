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
        return (
            f"Customer: {self.name}\n
            Subscription: {self.membership_type} member")

    def __repr__(self) -> str:
        """ Repr method
        """
        pass

    def update_membership(self, new_membership):
        """ Update a member's sub plan.
        """
        print("Updating your membership...")
        self.membership_type = new_membership


customers = [
    Customer('Nelly', 'Gold'),
    Customer('Tivere', 'Premiumest')
]

print(customers[0])
