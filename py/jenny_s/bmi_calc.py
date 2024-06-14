#!/usr/bin/python3

weight = int(input("Enter your weight in kg : "))
height = float(input("Enter your height in meters : "))

bmi = round(weight / pow(height, 2), 2)
print(f"\nYour Body-Mass Index is {bmi}\n")

if bmi < 16.8:
    print("You are severe underweight")
elif bmi < 18.4:
    print("You are underweight (Mild thinness)")
elif bmi < 25:
    print("Soft life.!! You're in perfect shape.")
elif bmi < 30:
    print("Take it easy now! You're getting overweight!!")
else:
    print("It's time to hit the gym and eat right!!!\nYou are OBESE")
