#! usr/bin/python3


# Because these functions are indented under the class Shark, they are called methods. Methods are a special kind of function that are defined within a class.


class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")

    def is_a_minor(self):
        print(f"{self.name} is a minor. He's only {self.age}")

def main():
    # Set name of Shark object
    sammy = Shark("Sammy", 12)
    efe = Shark("Efe", 17)
    sammy.swim()
    # sammy.be_awesome()
    efe.is_a_minor()

if __name__ == "__main__":
    main()
