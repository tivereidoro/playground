#!/usr/bin/python3


# Converts a string into a secret message.

# first take a string
print()
message = input("Enter a text to hide : ")

#set the variable to empty
secret_message = ""

#cycle thru and convert to unicode
for char in message:
    secret_message += str(ord(char) - 23)

print(f"\nYour secret message is {secret_message}.")

#cycle thru in pairs
original_message = ""

for num in range(0, len(secret_message)-1, 2):
    #get the 1st and 2nd digits of each
    char_code = secret_message[num] + secret_message[num+1]


    original_message += chr(int(char_code) + 23)

#back to original message attempt
print(f"\nYour actual message was '{original_message}'")
