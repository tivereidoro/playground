#!/usr/bin/python3
# Program to change the inputted matrix position
# to 'X'

print("You can change the value of a position..")
print("The position is in the format (rows,column).\n")
row_number = int(input("Enter the matrix position: "))
column_number = int(input("Enter the matrix position: "))

matrix = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
print(f"\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}")

matrix[row_number-1][column_number-1] = 'X'
print(f"\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
