#! usr/bin/python3


# Because these functions are indented under the class Shark, they are called methods. Methods are a special kind of function that are defined within a class.

class Shark:
    def swim(self):
        print("The shark swims")

    def be_awesome(self):
        print("The shark is being awesome.")


def main():
    sammy = Shark()
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()
