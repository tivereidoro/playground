#!/usr/bin/python3


# Converts a string into a secret message.

#take a string
message = input("Enter a text in UPPERCASE : ")

secret_message = ''

#cycle thru and convert to unicode
for char in message:
    secret_message += str(ord(char))

print(f"\nYour secret message is {secret_message}.")

#cycle thru in pairs

original_message = ""

for num in range(0, len(secret_message)-1, 2):
    #get the 1st and 2nd digits of each
    char_code = secret_message[num] + secret_message[num+1]


    original_message += chr(int(char_code))

#back to original message 
print(f"\nYour actual message was '{original_message}'")

