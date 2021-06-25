"""
File: complement.py
Name: Irene Chen 陳筱涵
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    post-condition: old DNA strand will be replaced with complement DNA
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    new_dna = build_complement(dna)
    print('The complement of '+str(dna)+' is '+str(new_dna))


def build_complement(dna):
    """
    post-condition: A will be replaced with T, and vice versa. C will be replaced with G, and vice versa.
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        if base == 'G':
            ans += 'C'
        elif base == 'C':
            ans += 'G'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
