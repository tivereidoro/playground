#!/usr/bin/python3

class Person():
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    
    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    

p1 = Person('Jude', 28, 'male')
print(p1)
