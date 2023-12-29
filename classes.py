#! usr/bin/python3


# Because these functions are indented under the class Shark, they are called methods. Methods are a special kind of function that are defined within a class.


class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")


def main():
    # Set name of Shark object
    sammy = Shark("Sammy")
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()
