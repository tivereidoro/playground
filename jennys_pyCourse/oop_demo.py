#!/usr/bin/python3

class Instructors:
    def __init__(self, ins_name, ins_location) -> None:
        self.name = ins_name
        self.address = ins_location

    def salute(self):
        print(f"Hello there {self.name} from {self.address}")

Tuva = Instructors('Tuva', 'South Africa')
Tuva.salute()
