#!/usr/bin/python3
import random
import string
'''
Program to generate ramdom password from user.'''
print("Welcome!!\nLet's generate a secured password for you!!\n")

# Accept the user's input prefernce for the password
letters = int(input("How many letters will you like in your password.?  "))
symbols = int(input("How many symbols should be in your password.?  "))
numbers = int(input("How many numbers will you like in your password.?  "))
# Generate the lists of alpha-numeric-symbols characters to choose from
alphabet_list = list(string.ascii_letters)
symbols_list = list(string.punctuation)
digit_list = list(string.digits)
# Init the random char variables
pswd_letters, pswd_symb, pswd_digit = "", "", ""

for i in range(letters):
    pswd_letters += random.choice(alphabet_list)
for j in range(symbols):
    pswd_symb += random.choice(symbols_list)
for k in range(numbers):
    pswd_digit += random.choice(digit_list)

password = list(pswd_letters + pswd_symb + pswd_digit)
random.shuffle(password)
password = ''.join(password)
print(f"\nYour secured password is {password}")
