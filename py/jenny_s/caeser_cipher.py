#!/usr/bin/python3
from cipher import encrypt, decrypt

while True:
    print("\nWelcome to Caeser's Cipher *#️**🔐\n")
    while True:
        option = input("Type 'E' for encryption OR Type 'D' for decryption.: ").upper()
        if option == 'E' or option == 'D':
            break

    print(option)
    text = input("Type the text to be ciphered below: \n").lower()
    shift = int(input("Enter cipher key **(number between 1 - 9): "))

    # Call the appropriate function
    if option == 'E':
        cipher_text = encrypt(plain_text=text, shift_key=shift)
        print(f"\nYour encrypted text is :\n{cipher_text}\n\nSuccess ✔✔\n")
    elif option == 'D':
        plain_text = decrypt(cipher_text=text, shift_key=shift)
        print(f"\nYour decrypted text is :\n{plain_text}\n\nSuccess ✔✔\n")

    # Validate restart or quitting
    while True:
        stat = input("Type 'Y' to go again OR Type 'N' to quit.: ").upper()
        if stat == 'Y' or stat == 'N':
            break
    if stat == 'Y':
        continue
    else:
        print("\nTerminating cipher..🫡 🫡 \nGoodbye ...")
        break
