#!/usr/bin/python3

class University:
    def __init__(self, name):
        print("Initializing from University")
        self.uni_name = name

    def show_details(self):
        print(f"This is {self.uni_name}")

class Course(University):
    def __init__(self, name):
        super().__init__(name)
        self.crs_name = name
        print("Displaying from Course class")

    def show_details(self):
        super().show_details()
        print(f"This is {self.crs_name}")

class Branch(University):
    def show(self):
        print("Hi from C class")

class Student(Course, Branch):
    def display(self):
        print("Displaying from D class")

class Faculty(Branch):
    ...


u1 = University('Uniben')
u1.show_details()

c1 = Course('SLT')
c1.show_details()
