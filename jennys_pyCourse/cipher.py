#!/usr/bin/python3
# Ecrpt = (X + n) mod 26
# Dcrpt = (X - n) mod 26
import string
alphabet_list = list(string.ascii_lowercase)
print(alphabet_list)


def encrypt(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        position = alphabet_list.index(char)
        new_position = (position + shift_key) % 26
        cipher_text += alphabet_list[new_position]

    return cipher_text


def decrypt(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        position = alphabet_list.index(char)
        new_position = (position - shift_key) % 26
        plain_text += alphabet_list[new_position]

    return plain_text
