"""
File: caesar.py
Name: Irene Chen 陳筱涵
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Post- condition: try to find the ALPHABET from the created new alphabet.
    """
    secret = int(input('Secret Number: '))
    first_new = ALPHABET[len(ALPHABET)-secret:]
    second_new = ALPHABET[0:len(ALPHABET)-secret]
    new_alphabet = first_new + second_new
    word = input("What's the ciphered string? ")
    ans = ""
    for word_item in word:
        number = new_alphabet.find(word_item.upper())
        if word_item.isalpha():
            new_word = ALPHABET[number]
            ans += new_word.upper()
        else:
            ans += word_item
    print('The deciphered string is :'+ans+'!')



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
