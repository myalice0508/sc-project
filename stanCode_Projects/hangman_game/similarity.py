"""
File: similarity.py
Name: Irene Chen 陳筱涵
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Post-condition: to find the higher similar word in the DNA sequence
    """
    long_sequence = str(input('Please give me a DNA sequence to search: '))
    short_sequence = str(input('What DNA sequence would you like to match: '))
    count_l = len(long_sequence)
    count_s = len(short_sequence)
    best_match = ""
    worse = ""
    word = ""
    not_match = ""

    for i in range(count_l-count_s+1):
        check1 = long_sequence[i:count_s+i]

        for j in range(len(check1)):
            ls = check1[j].upper()
            ss = short_sequence[j].upper()
            if ls == ss:
                word += ls
            else:
                word += ls
                not_match += ls

        if best_match == "":
            worse = not_match
            best_match = word
        else:
            if len(not_match) < len(worse):
                # which one has less not match word
                worse = not_match
                best_match = word
        word = ""
        not_match = ""

    print('The best match is '+ str(best_match))









    # print(check1)
    # print(ch)
    # print(sh)




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
