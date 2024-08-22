#!/usr/bin/python3
from csv import reader, writer, DictReader, DictWriter

def main():
    with open("dump.csv") as file:
        read = DictReader(file)
        for line in read:
            print(f"{line['username']} got {line['grade']} grade.")


# Call main
if __name__ == "__main__":
    main()
