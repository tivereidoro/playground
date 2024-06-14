#!/usr/bin/python3
# Check whether a given year is leap year or not.

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")


if __name__ == '__main__':
    pass
