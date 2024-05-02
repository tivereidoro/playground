#!/usr/bin/python3
# Ankit Rao  Nisha Jain

print("Hello! This is the Love Calculator.\n")
you = input("What is your name.? (Full name preferably): ")
them = input("\nWho do you want to match with.? (Full name preferably): ")

joint_name = (you + them).strip().lower().replace(" ", "")
print(joint_name)

true = joint_name.count('t') + joint_name.count('r') + joint_name.count('u') + joint_name.count('e')
love = joint_name.count('l') + joint_name.count('o') + joint_name.count('v') + joint_name.count('e')

score = true*10 + love
print(f"\nYou and {them} have a love score of {score}%")
